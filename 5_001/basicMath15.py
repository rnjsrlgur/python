# 순열의 값을 구하기
numN = int(input('n : '))
numR = int(input('r : '))
result = 1

for n in range(numN, (numN - numR), -1):
    print('n : {}'.format(n))
    result = result * n

print('result: {}'.format(result))

# 원순열
# n명의 친구가 원탁 테이블에 앉을수 있는 순서를 계산하는 프로그램

n = int(input('친구수 : '))
result = 1
for i in range(1, n):
    result *= i
    
print('result: {}'.format(result))