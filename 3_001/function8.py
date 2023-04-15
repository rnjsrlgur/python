# global키워드를 이용하면 함수 안에서도 전역변수의 값을 수정할 수 있다.
num_out = 10


def printNum():
    global num_out
    num_out = 20
    print(f'num_out: {num_out}')

printNum()
print(f'num_out: {num_out}')