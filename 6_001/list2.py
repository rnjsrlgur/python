# 5명의 학생이름을 리스트에 저장하고 인덱스가 홀수인 학생과 짝수인 학생을 구분해서 인덱스와 학생 이름 출력.

students = ['유재석', '박명수', '정준하', '하하', '김종국']
print('인덱스가 짝수인 학생')
print('students[0] : {}'.format(students[0]))
print('students[2] : {}'.format(students[2]))
print('students[4] : {}'.format(students[4]))

print('인덱스가 홀수인 학생')
print('students[1] : {}'.format(students[1]))
print('students[3] : {}'.format(students[3]))

# for문으로 변경
for i in range(len(students)):
    if i % 2 == 0:
        print('인덱스가 짝수인 학생')
        print('index : students[{}] : {}'.format(i, students[i]))
    else:
        print('인덱스가 홀수인 학생')
        print('index : students[{}] : {}'.format(i, students[i]))