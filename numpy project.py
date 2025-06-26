import numpy as np

# Marks of 5 students in 4 subjects (out of 100)
marks = np.array([
    [78, 85, 90, 88],
    [60, 72, 68, 70],
    [92, 88, 95, 91],
    [55, 60, 58, 62],
    [80, 85, 84, 83]
])
students = np.array(["Sujoy", "Shubham", "Boss", "Sam", "Yogi"])
subjects = np.array(["Math", "Physics", "Chemistry", "Biology"])

student_totals = marks.sum(axis=1)
student_averages = marks.mean(axis=1)
print(student_totals, "\n")
print(student_averages, "\n")

subject_averages = marks.mean(axis=0)
topper_index = np.argmax(student_totals)
print("Topper:", students[topper_index], "\n")

normalized_marks = (marks - marks.min()) / (marks.max() - marks.min())
print(normalized_marks, "\n")

pass_mask = marks >= 40
student_pass_status = pass_mask.all(axis=1)  # True if passed all subjects
print(student_pass_status)