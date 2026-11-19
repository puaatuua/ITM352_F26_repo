# Using Pytest to test the quiz web application
# This code was written by Copilot and modified by me to include addtional tests and to fix errors in the original code.

# Name: Ava Puaatuua
# Date: Nov. 18, 2026

import pytest

from quiz_webapp import app, load_scores, prepare_questions


@pytest.fixture
def client():
    app.config.update(
        TESTING=True,
        SECRET_KEY="test-secret"
    )

    with app.test_client() as test_client:
        yield test_client

# Test question loading and filtering
def test_question_loading():
    questions = __import__("quiz_webapp").load_questions()

    assert isinstance(questions, list)
    assert len(questions) > 0


def test_prepare_questions_filters_by_difficulty():
    questions = __import__("quiz_webapp").load_questions()

    prepared = prepare_questions(
        questions,
        category="All",
        difficulty="Easy"
    )

    assert prepared
    assert all(
        question["difficulty"].lower() == "easy"
        for question in prepared
    )

# Test Flask routes
def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Welcome" in response.data


def test_setup_page(client):
    response = client.get("/setup")

    assert response.status_code == 200
    assert b"Category" in response.data
    assert b"Difficulty" in response.data


def test_question_api(client):
    response = client.get("/api/questions")

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

# Test score API
def test_invalid_score_api(client):
    response = client.post(
        "/api/scores",
        json={"score": "eight", "total": 10}
    )

    assert response.status_code == 400


def test_valid_score_api(client):
    response = client.post(
        "/api/scores",
        json={"score": 8, "total": 10}
    )

    assert response.status_code == 201
    assert response.get_json()["score"] == 8

# Test score-loading error handling
def test_empty_score_file_handling(tmp_path, monkeypatch):
    import quiz_webapp

    empty_file = tmp_path / "scores.json"
    empty_file.write_text("", encoding="utf-8")

    monkeypatch.setattr(
        quiz_webapp,
        "SCORE_FILE",
        empty_file
    )

    assert quiz_webapp.load_scores() == []

# Test quiz session flow
def test_setup_creates_quiz_session(client):
    response = client.post(
        "/setup",
        data={
            "category": "Basketball",
            "difficulty": "Medium"
        }
    )

    assert response.status_code == 302

    with client.session_transaction() as stored_session:
        assert "questions" in stored_session
        assert stored_session["question_index"] == 0
        assert stored_session["score"] == 0
