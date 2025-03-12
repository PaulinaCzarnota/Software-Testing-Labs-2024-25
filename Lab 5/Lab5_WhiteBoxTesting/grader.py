import math

def get_grade_classification(grade):
    """
    Classifies a student's grade according to the grading scale.

    :param grade: int or float - The student's grade (0-100)
    :return: str - Classification ("Fail", "Pass", "2.ii", "2.i", "1")

    Grading Criteria:
    - 0 to 39  → "Fail"
    - 40 to 49 → "Pass"
    - 50 to 59 → "2.ii"
    - 60 to 69 → "2.i"
    - 70 to 100 → "1"

    Raises:
    - ValueError: If input is not a number, NaN, or not in the valid range (0-100).
    """

    # Ensure the input is a number (int or float) but NOT a boolean
    if not isinstance(grade, (int, float)) or isinstance(grade, bool) or math.isnan(grade):
        raise ValueError("Grade must be a number (int or float), and not NaN.")

    # Ensure grade is within the valid range (0 to 100)
    if grade < 0 or grade > 100:
        raise ValueError("Grade must be between 0 and 100.")

    # Apply grading classification logic
    if 0 <= grade < 40:
        return "Fail"
    elif 40 <= grade < 50:
        return "Pass"
    elif 50 <= grade < 60:
        return "2.ii"
    elif 60 <= grade < 70:
        return "2.i"
    else:
        return "1"