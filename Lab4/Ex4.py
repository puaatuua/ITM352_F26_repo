# Try to append to a tuple. It won't work.

# Name: Ava Puaatuua
# Date: Sept. 16, 2026

survey_respondents = (1012, 1035, 1021, 1053)
# survey_respondents.append(1054)

survey_respondents = survey_respondents + (1054,)
print("Updated survey respondents:", survey_respondents)

