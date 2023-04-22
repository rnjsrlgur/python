# 군수열
# n번째 항의 값 출력
# {1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, ...}

inputN = int(input('n : '))

flag = True
n = 1; nCnt = 1; searchN = 0
while flag:
    for i in range(1, (n + 1)):
        if i == n:
            print('{} '.format(i), end='')
        else:
            print('{} '.format(i), end='')

        nCnt += 1

        if(nCnt > inputN):
            searchN = i
            flag = False
            break

    print()
    n += 1

print('{}항 : {}'.format(inputN, searchN))