# 반복문 대신 재귀 함수를 이용한 예
def recusion(num):

    if num > 0:
        print('*' * num)
        return recusion(num - 1)

    else:
        return 1

recusion(10)

# 재귀 함수를 이용한 팩토리얼 구하기

def factorial(num):

    if num > 0:
        return num *  factorial(num - 1)

    else:
        return 1

print(f'factorial(10): {factorial(10)}')