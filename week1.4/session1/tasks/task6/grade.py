# Week 4, Session 1: Task 3

# You are given function calculate_grade and a docstring.
# Your task is to write the body of the function based on the
# details in the docstring


def calculate_grade(marks):
    """
    This function returns a grade based on the provided mark, according to
    the following grading scale:

    Grading Rules:
    - marks < 50: grade is 'F'
    - marks >= 50 and < 60: grade is 'D'
    - marks >= 60 and < 70: grade is 'C'
    - marks >= 70 and < 80: grade is 'B'
    - marks >= 80: grade is 'A'

    Validity Checks:
    - Returns `None` if `marks` is not a valid positive integer between
      0 and 100 (inclusive)
    - Returns `None` if `marks` is greater than 100, as it falls outside
      the valid range

    Args:
        marks (int): A positive integer representing the student's marks.
        Valid range is 0 to 100 (inclusive)

    Returns:
        str: The grade corresponding to the marks ('A', 'B', 'C', 'D', 'F').
        None: If `marks` is not a valid integer or is outside the allowed
              range (greater than 100 or negative)
    """
    grade=""

    # validity checks
    if type(marks) != int: # not an int
        return None
    if marks>100 or marks <0: # outside the range/not positive
        return None

    if marks < 50:
        grade = 'F'
    if marks >= 50 and marks< 60:
        grade = 'D'
    if marks >= 60 and marks< 70:
        grade = 'C'
    if marks >= 70 and marks< 80:
        grade = 'B'
    if marks >= 80:
        grade = 'A'

    return grade


# Check if the following tests produce the correct output
print(calculate_grade(39))
print(calculate_grade(55))
print(calculate_grade(-20))
print(calculate_grade(100))
