# 출퇴근 시 이용하는 교통 수단에 따라 세금을 감면해주는 정책을 세우려 한다. 다음 내용에 맞게 프로그램 작성
'''
출퇴근 대상인가?
출퇴근 대상이면
    도보, 자전거 -> 세금 감면 5%
    버스, 지하철 -> 세금 감면 3%
    자가용 -> 추가 세금 1%

출퇴근 대상자가 아니면
    세금 변동 없음.
'''

userInput = int(input('출퇴근 대상 여부 [1. Yes \t 2. No] : '))

if userInput == 1:
    print('교통 수단을 선택하세요')
    trans = int(input('[1. 도보, 자건거 \t 2. 버스, 지하철, \t 3. 자가용] : '))

    if trans == 1:
        print('세금 감면 5%')
    elif trans == 2:
        print('세금 감면 3%')
    elif trans == 3:
        print('추가 세금 1%')
    else:
        print('잘못 입력하였습니다.')
elif userInput == 2:
    print('세금 변동 없음.')
else:
    print('잘못 입력하였습니다.')