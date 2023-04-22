# 등비 수열
# n번째 항까지의 합 출력
# {5, 15, 45, 135, 405, 1215, ...}

# 등비 수열
# n번째 항의 값을 출력
# {2, 4, 8, 16, 32, 64, 128, ...}

a1 = int(input('첫번째 항 : '))
r = int(input('공비 : '))
n = int(input('n : '))

value = 0
sumN = 0
m = 1
while m <= n:
    if m == 1:
        value = a1
        sumN += value
        print('{}번째 항의 값 : {}'.format(m, sumN))
        m += 1
        continue

    value *= r
    sumN += value
    print('{}번째 항의 값 : {}'.format(m, sumN))
    m += 1

print('{}번째 항의 값 : {}'.format(n, sumN))