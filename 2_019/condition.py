# 키오스크에서 메뉴를 선택하면 영수증이 출력되는 프로그램 만들기.

print('1. 카페라떼(3.5) \t 2.에스프레소(3.0) \t 3. 아메리카노(2.0) \t 4. 카페라떼(4.0)')
userChoice = int(input('메뉴 번호 입력 : '))
print('-' * 25)
if userChoice == 1:
    print('카페라떼(3.5)를 선택하였습니다.')
    print('가격 : {}'.format(3500, ','))
elif userChoice == 2:
    print('에스프레소(3.0)를 선택하였습니다.')
    print('가격 : {}'.format(3000, ','))
elif userChoice == 3:
    print('아메리카노(2.0)를 선택하였습니다.')
    print('가격 : {}'.format(2000, ','))
elif userChoice == 4:
    print('카페라떼(4.0)를 선택하였습니다.')
    print('가격 : {}'.format(4000, ','))
print('-' * 25)