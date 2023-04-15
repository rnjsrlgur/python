# 구구단 출력
def gugudan2():
    for i in range(1, 10):
        print('2 * {} = {}'.format(i, 2 * i))
    gugudan3()


def gugudan3():
    for i in range(1, 10):
        print('3 * {} = {}'.format(i, 3 * i))
    gugudan4()


def gugudan4():
    for i in range(1, 10):
        print('4 * {} = {}'.format(i, 4 * i))


gugudan2()