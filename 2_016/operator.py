# 백신 접종 대상자는 20세 미만 또는 65세 이상자에 한합니다. 를 논리 연산자를 이용해 코딩
age = int(input('age : '))
vaccine = (age < 20) or (age >= 65)
print('age : {}, vaccine : {}'.format(age, vaccine))