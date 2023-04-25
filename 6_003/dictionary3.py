# 0부터 10까지의 각각의 정수에 대한 팩토리얼을 딕셔너리에 추가.
factorialDic = {}

for i in range(11):
    if i == 0:
        factorialDic[i] = 1
    else:
        for j in range(1, (i + 1)):
            factorialDic[i] = factorialDic[i - 1] * j

print(f'factorialDic : {factorialDic}')