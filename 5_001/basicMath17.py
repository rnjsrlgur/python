# 확률
# 박스에 '꽝'이 적힌 종이가 4장 있고, '선물'이 적힌 종이가 3장이 있을 때,
# 파이썬을 이용해 꽝 2장과 선물 1장을 뽑는 확률
def proFun():

    numN = int(input('numN : '))
    numR = int(input('numR : '))

    resultP = 1
    resultR = 1
    resultC = 1

    for n in range(numN, (numN - numR), -1):
        resultP = resultP * n
    print('resultP : {}'.format(resultP))

    for n in range(numR, 0, -1):
        resultR = resultR * n
    print('resultR : {}'.format(resultR))

    resultC = int(resultP / resultR)
    print('resultC : {}'.format(resultC))

    return resultC

sample = proFun()
print('sample : {}'.format(sample))

event1 = proFun()
print('event1 : {}'.format(event1))

event2 = proFun()
print('event2 : {}'.format(event2))

probability = (event1 * event2) / sample
print('probability : {}%'.format(round(probability * 100, 2)))