# while 조건식:
# 	실행문

# while문을 이용하여 사용자가 입력한 구구단 출력
gugudan = int(input('단 : '))

n = 1
while n < 10:
    result = gugudan * n
    print('{} * {} = {}'.format(gugudan, n, result))
    n += 1

# 구구단 전체 출력
for i in range(1, 10): # 1 ~ 9까지의 범위 반복 -> 곱할 값
    for j in range(2, 10): # 2 ~ 9까지의 범위 반복 -> 단
        result = j * i
        print('{} * {} = {}\t'.format(j, i, result), end='')
    print()