student_name = input("Enter student name: ")
subjects = ["Math", "Science", "English", "Hindi", "Computer"]
marks = {}

for subject in subjects:
    mark = int(input(f"Enter marks for {subject} (out of 100): "))
    marks[subject] = mark

print(marks)

total = sum(marks.values())
percentage = total / len(subjects)

print(f"Total Marks: {total} / {len(subjects) * 100}")
print(f"Percentage: {percentage}%")

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")

print("----------------------------")
print(f"Student Name: {student_name}")
print("----------------------------")
for subject, mark in marks.items():
    print(f"{subject}: {mark}/100")
print("----------------------------")
print(f"Total: {total}/{len(subjects) * 100}")
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")
print("----------------------------")