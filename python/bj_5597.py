student_list = [i for i in range(1, 31)]

for _ in range(1, 29):
    student = int(input())
    student_list.remove(student)

print(student_list[0])
print(student_list[1])
