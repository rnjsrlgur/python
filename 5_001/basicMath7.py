# 등차 수열
# n번째 항의 값을 출력
# {2, 5, 8, 11, 14, 17, 20, 23, 26, 29}

a1 = int(input('a1 : '))
d = int(input('d : '))
n1 = int(input('n1 : '))

valueN = 0
n = 1
while n <= n1:
    if n == 1:
        valueN = a1
        print('{}번째 항의 값 : {}'.format(n, valueN))
        n += 1
        continue

    valueN += d
    print('{}번째 항의 값 : {}'.format(n, valueN))
    n += 1

print('{}번째 항의 값 : {}'.format(n1, valueN))