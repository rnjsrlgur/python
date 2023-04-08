import math

# 제곱근 : sqrt()
print('2의 제곱근 : %.2f' % math.sqrt(2))

# 거듭제곱 : pow()
print('2의 3제곱 : %.2f' % math.pow(2, 3))

# 아들이 엄마한테 용돈을 받는데, 첫 달에는 200원을 받고 매월 이전 달의 2배씩 인상하기로 했다. 12개월 째 되는 달에는 얼마를 받을 수 있는지 출력
firstMoney = 200
after12Months = ((firstMoney * 0.01) ** 12) * 100
print('12개월후 받는 용돈 : %.f원' % after12Months)

after12Months = int(after12Months)
after12MonthsFormat = format(after12Months, ',')

print('12개월후 받는 용돈 : %s원' % after12MonthsFormat)