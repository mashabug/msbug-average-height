student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0

for height in student_heights:
  total_height += height
print(f"The total height = {total_height}")

total_students = 0

for student in student_heights:
  total_students += 1
print(f"The total of students = {total_students}")

average_height = round(total_height / total_students)
print(f"Average height = {average_height}")
