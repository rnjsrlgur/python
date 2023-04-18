# 세 개의 수를 입력하면 최소 공배수를 출력
num1 = int(input('num1 : '))
num2 = int(input('num2 : '))
num3 = int(input('num3 : '))

maxNum = 0

for i in range(1, num1 + 1):
    if num1 % i == 0 and num2 % i == 0:
        maxNum = i

print('{}과 {}의 최대공약수 : {}'.format(num1, num2, maxNum))

minNum = (num1 * num2) // maxNum
print('{}과 {}의 최소공배수 : {}'.format(num1, num2, maxNum))

newNum = minNum
for i in range(1, (newNum + 1)):
    if newNum % i == 0 and num3 % i == 0:
        maxNum = i

print('최대공약수 : {}'.format(maxNum))

minNum = (newNum * num3) // maxNum
print('{}, {}, {}의 최대공배수 : {}'.format(num1, num2, num3, minNum))

# 섬마을에 과일, 생선, 야채를 판매하는 배가 다음 주기로 입항한다. 모든 배가 입항하는 날짜를 계산
# 과일 선박: 3일, 생선 선박:4일, 야채 선박:5일

fr = 3; fi = 4; ve = 5
maxDay = 0

for i in range(1, fr + 1):
    if fr % i == 0 and fi % i == 0:
        maxDay = i # 과일, 생선 배의 최대공약수

minDay = (fr * fi) // maxDay # 과일, 생선 배의 최소공배수

newDay = minDay

for i in range(1, newDay + 1):
    if newDay % i == 0 and ve % i == 0:
        maxDay = i

minDay = (newDay * ve) // maxDay

print('세 대의 배는 {}일 마다 모두 입항한다.'.format(maxDay))
