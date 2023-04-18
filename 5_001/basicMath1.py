# 사용자가 입력한 숫자의 약수 출력

userInput = int(input('숫자 입력 : '))

for num in range(1, (userInput + 1)):
    if userInput % num == 0:
        print('{}의 약수 : {}'.format(userInput, num)) # 나머지가 0인 숫자 찾기

print('---')

# 사용자가 입력한 숫자의 소수

for num in range(2, (userInput + 1)):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break

    if (flag):
        print('{}의 소수 : {}'.format(userInput, num))
    else:
        print('{}의 합성수 : {}'.format(userInput, num))
