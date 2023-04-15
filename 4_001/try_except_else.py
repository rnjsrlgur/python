# 사용자로부터 숫자 5개를 입력받아, 짝수, 홀수, 실수로 구분해서 각각을 리스트에 저장하는 프로그램 작성

eveList = []
oddList = []
floatList = []

n = 1
while n < 6:
    try:
        num = float(input('숫자 입력 : '))

    except:
        print('예외 발생!')
        print('다시 입력하세요 ')
        continue

    else:
        if num - int(num) != 0:
            print('Float')
            floatList.append(num)
        else:
            if num % 2 == 0:
                print('even')
                eveList.append(int(num))
            else:
                print('odd')
                oddList.append(int(num))
        n += 1

print(f'floatList: {floatList}')
print(f'eveList: {eveList}')
print(f'oddList: {oddList}')
