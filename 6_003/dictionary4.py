# 하루에 몸무게(kg)와 신장(m) 이 각각 -0.3kg, +0.001m씩 변한다고 할 때, 30일 후의 몸무게와 신장의 값을 저장하고, BMI값도 출력하는 프로그램.

bodyInfo = {'name':'darim', 'weight':83.0, 'height':1.8}

myBMI = bodyInfo['weight'] / (bodyInfo['height'] ** 2)

print(f'bodyInfo:{bodyInfo}')
print(f'BMI:{round(myBMI, 2)}')