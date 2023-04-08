# random과 operator 모듈을 사용해서 10 ~ 100 사이의 난수 중 십의 자리와 일의 자리가 각각 3의 배수인지 판단하는 코드 작성

import random
import operator

rInt = random.randint(10, 100)

num1 = operator.floordiv(rInt, 10) # 10의 자릿수 추출 (10으로 나눈 몫)
num2 = operator.mod(rInt, 10) # 1의 자릿수 추출 (10으로 나눈 나머지)

print('난수 : {}'.format(rInt))
print('십의 자리 : {}'.format(num1))
print('일의 자리 : {}'.format(num2))

print()

print('십의 자리는 3의 배수 : {}'.format(operator.mod(num1, 3) == 0))
print('일의 자리는 3의 배수 : {}'.format(operator.mod(num2, 3) == 0))