def grading_students(grades):
    """
    Apply HackerLand University’s rounding policy to student grades.

    Given `grades`, a list of integers in the range 0–100, this function rounds each student's 
    grade according to Sam’s rules:

      • If a grade is less than 38, it remains unchanged (still a failing grade).
      • Otherwise, if the difference between the grade and the next multiple of 5 is less than 3,
        round the grade up to that multiple; otherwise, leave it as is.

    Parameters:
        grades (List[int]): List of integer grades (each between 0 and 100 inclusive)

    Returns:
        List[int]: List of grades after applying the rounding policy

    Example:
        Input: [73, 67, 38, 33]
        Processing:
          - 73 → next multiple of 5 is 75; difference is 2 (<3) → rounded to 75
          - 67 → next multiple is 70; difference is 3 (not <3) → remains 67
          - 38 → next multiple is 40; difference is 2 (<3) → rounded to 40
          - 33 → below 38 → remains 33
        Output: [75, 67, 40, 33]
    """

    for i,g in enumerate(grades):
        if grades[i] >= 38:
            res = 5 - (grades[i] % 5)
            if res < 3:
                grades[i] = grades[i] + res
    return grades
            