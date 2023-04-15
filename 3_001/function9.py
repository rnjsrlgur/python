# calculator()를 선언하고 calculator() 안에 사칙연산 함수를 선언
def calculator(n1, n2, operator):
    def add():
        print(f'덧셈 : {round(n1 + n2, 2)}')
    def sub():
        print(f'뺄셈 : {round(n1 - n2, 2)}')
    def mul():
        print(f'곱셈 : {round(n1 * n2, 2)}')
    def div():
        print(f'나눗셈 : {round(n1 / n2, 2)}')


    if operator == 1:
        add()
    elif operator == 2:
        sub()
    elif operator == 3:
        mul()
    elif operator == 4:
        div()

while True:
    num1 = float(input('n1 : '))
    num2 = float(input('n2 : '))
    operatorNum = int(input('1(+), 2(-), 3(*), 4(/), 5(종료) : '))

    if operatorNum == 5:
        break

calculator(num1, num2, operatorNum)