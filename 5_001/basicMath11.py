# 계차 수열
# n번째 항의 값을 출력
# {3, 7, 13, 21, 31, 43, 57}
# {4, 6, 8, 10, 12, 14}

an1 = int(input('a1 : '))
an = int(input('an : '))

bn1 = int(input('bn1 : '))
bd = int(input('bn 공차 : '))

valueAN = 0
valueBN = 0

n=1

while n <= an:

    if n == 1:
        valueAN = an1
        valueBN = bn1
        print('an의 {}번째 항의 값 : {}'.format(n, valueAN))
        print('bn의 {}번째 항의 값 : {}'.format(n, valueBN))
        n += 1
        continue

    valueAN = valueAN + valueBN
    valueBN =  valueBN + bd
    print('an의 {}번째 항의 값 : {}'.format(n, valueAN))
    print('bn의 {}번째 항의 값 : {}'.format(n, valueBN))
    n += 1

print('an의 {}번째 항의 값 : {}'.format(an, valueAN))
print('bn의 {}번째 항의 값 : {}'.format(an, valueBN))

