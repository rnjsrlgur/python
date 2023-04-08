num1 = 10
num2 = 40

result = num1 < num2
print('num1 < num2 : {}'.format(result))

result = num1 > num2
print('num1 > num2 : {}'.format(result))

result = num1 <= num2
print('num1 <= num2 : {}'.format(result))

result = num1 >= num2
print('num1 >= num2 : {}'.format(result))

result = num1 == num2
print('num1 == num2 : {}'.format(result))

result = num1 != num2
print('num1 != num2 : {}'.format(result))
print()
userInputNum1 = int(input('숫자 1 입력 : '))
userInputNum2 = int(input('숫자 2 입력 : '))
print('-' * 20)
print('{} < {} : {}'.format(userInputNum1, userInputNum2, (userInputNum1 < userInputNum2)))
print('{} <= {} : {}'.format(userInputNum1, userInputNum2, (userInputNum1 <= userInputNum2)))
print('{} > {} : {}'.format(userInputNum1, userInputNum2, (userInputNum1 > userInputNum2)))
print('{} >= {} : {}'.format(userInputNum1, userInputNum2, (userInputNum1 >= userInputNum2)))
print('{} == {} : {}'.format(userInputNum1, userInputNum2, (userInputNum1 == userInputNum2)))
print('{} != {} : {}'.format(userInputNum1, userInputNum2, (userInputNum1 != userInputNum2)))
print('-' * 20)

