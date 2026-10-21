# Part 6: File Path Operations
# Create a program that safely checks for and creates files/directories

from pathlib import Path

data_directory = Path("data")
data_directory.mkdir(parents=True, exist_ok=True)

file_path = data_directory / "example.txt"

if not file_path.exists():
    file_path.write_text("Created safely.\n", encoding="utf-8")
    print(f"Created {file_path}")
else:
    print(f"{file_path} already exists.")

if file_path.is_file():
    print(file_path.read_text(encoding="utf-8"))
