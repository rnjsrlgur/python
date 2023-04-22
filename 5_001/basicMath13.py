# 팩토리얼
inputN = int(input('n : '))
##########################################
# for 문

result = 1
for n in range(1, inputN + 1):
    result *= n

print('{}! : {}'.format(inputN, result))

##########################################
# while 문
n = 1
while n <= inputN:
    result *= n
n += 1

print('{}! : {}'.format(inputN, result))


##########################################
# 재귀함수
def factorialFun(n):
    if n == 1: return 1

    return n * factorialFun(n - 1)

print('{}! : {}'.format(inputN, factorialFun(inputN)))