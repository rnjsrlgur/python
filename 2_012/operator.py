num1 = 10
num2 = 3

result = num1 / num2

print('result : {}'.format(result))
print('result : %.2f' % result)

# 나머지
result = num1 % num2
print('result : {}'.format(result))

# 몫
result = num1 // num2
print('result : {}'.format(result))

# 나머지와 몫을 한번에 구하는 함수 divmod()
result = divmod(num1, num2)
print('result : {}'.format(result))
print('몫 : {}'.format(result[0]))
print('나머지 : {}'.format(result[1]))

# 123개의 사과를 4개씩 직원들에게 나누어 주려고 한다. 최대 나누어 줄 수 있는 직원수와 남는 사과 개수 출력
employee = 123
apple = 4
result = divmod(employee, apple)
print('사과를 나누어 줄 수 있는 최대 직원 수 : {}명'.format(result[0]))
print('남는 사과 : {}개'.format(result[1]))