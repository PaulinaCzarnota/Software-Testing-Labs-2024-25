# Calculating Grades

# This program collects 3 exam scores, calculates the average, determines the letter grade, and prints if the student is passing.

# Average	Grade
# 90+	    A
# 80-89	    B
# 70-79	    C
# 60-69	    D
# 0-59	    F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.


# Get valid integer inputs for three exams
exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: "))
exam_three = int(input("Input exam grade three: "))

# Store grades in a list
grades = [exam_one, exam_two, exam_three]
total = 0

# Sum the grades
for grade in grades:
    total += grade

# Calculate average
avg = total / len(grades)

# Determine letter grade based on average
if avg >= 90:
    letter_grade = "A"
elif avg >= 80:
    letter_grade = "B"
elif avg >= 70:
    letter_grade = "C"
elif avg >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Output each grade
for grade in grades:
    print("Exam: " + str(grade))

# Output average and letter grade
print("Average: " + str(avg))
print("Grade: " + letter_grade)

# Print pass/fail message
if letter_grade == "F":
    print("Student is failing.")
else:
    print("Student is passing.")