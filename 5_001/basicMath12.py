# 피보나치 수열
from anyio import value

inputN = int(input('n : '))

valueN = 0
sumN = 0

valN2 = 0
valN1 = 0

n = 1

while n <= inputN:

    if n == 1 or n == 2:
        valueN = 1
        valN2 = valueN
        valN1 = valueN
        sumN += valueN
        n += 1

    else:
        valueN = valN2 + valN1
        valN2 = valN1
        valN1 = valueN
        sumN += valueN
        n += 1

print('{}번째 항의 값 : {}'.format(inputN, valueN))
print('{}번째 항까지의 합 : {}'.format(inputN, sumN))