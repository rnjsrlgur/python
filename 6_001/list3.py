students = ['유재석', '박명수', '정준하', '하하', '김종국']

# for문
for i in range(len(students)):
    print('i : {}'.format(i))
    print('students[{}] : {}'.format(i, students[i]))

print()

# while문
n = 0
while n < len(students):
    print('n : {}'.format(n))
    print('students[{}] : {}'.format(n, students[n]))
    n += 1