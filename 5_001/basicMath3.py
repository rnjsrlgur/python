# 두개의 수를 입력하면 공약수와 최대공약수 출력

num1 = int(input('num1 : '))
num2 = int(input('num2 : '))

max_num = 0

for i in range(1, (num1 + 1)):
    if num1 % i == 0 and num2 % i == 0:
        print('공약수: {}'.format(i))
        max_num = i

print('최대공약수 : {}'.format(max_num))

print()

# 세개의 수를 입력 받아 공약수와 최대공약수 출력

num3 = int(input('num3 : '))

for i in range(1, (num1 + 1)):
    if num1 % i == 0 and num2 % i == 0 and num3 % i:
        print('공약수: {}'.format(i))
        max_num = i
print('최대공약수 : {}'.format(max_num))

# 유클리드 호제법을 이용해서 최대공약수 구하기
temp1 = num1; temp2 = num2

while temp2 > 0:
    temp = temp2
    temp2 = temp1 % temp2
    temp1 = temp
print('{} {}의 최대공약수 : {}'.format(num1, num2, temp1))

for n in range(1, (temp1 + 1)):
    if temp1 % n == 0:
        print('{} {} 의 공약수 : {}'.format(num1, num2, n))
