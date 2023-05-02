import random as rd
import bubbleSortMod as sm

students = []

for i in range(20):
    students.append(rd.randint(175, 185))

print(f'students : {students}')

sortedStudent = sm.bubbleSort(students, deepCopy=True)

print(f'students : {students}')
print(f'sortedStudents : {sortedStudent}')