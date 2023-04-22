# 등차 수열
# n번째 항까지의 합을 출력
# {5, 9, 13, 17, 21, 25, ...}

a1 = int(input('a1 : '))
d = int(input('d : '))
n1 = int(input('n1 : '))

valueN = 0
sumN = 0
n = 1

while n <= n1:

    if n == 1:
        valueN = a1
        sumN += valueN
        print('{}번째 항까지의 합 : {}'.format(n, sumN))
        n += 1
        continue

    valueN += d
    sumN += valueN
    print('{}번째 항까지의 합 : {}'.format(n, sumN))
    n += 1

print('{}번째 항까지의 합 : {}'.format(n1, sumN))