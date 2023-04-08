# Input Output : IO

print('데이터를 입력하세요.')
userInput = input()

print(userInput)

userInput2 = input('데이터를 입력하세요. : ')
print(userInput2)

# input()으로 입력받은 데이터는 모두 문자형 str

# print()
userName = 'user'
userAge = 26

print(userName)
print(userAge)

print('User : ', userName)
print('Age : ', userAge)

print('3 * 5 = ', end='') # end='' : print()는 자동 개행(\n)이 있지만, 자동 개행을 원치 않을 때, end='' 로 조건을 걸 수 있다.
print(3 * 5)

# formating
print(f'User : {userName}')
print(f'Age : {userAge}')