# 다음의 요구 사항을 해결하기 위해 조건식과 if ~ else문 중 알맞은 구문을 사용해보자.
# [요구사항]
# 1. 최저 기온 입력
# 2. 최고 기온 입력
# 3. 일교차가 11도 이상인 경우 출력 내용
# 일교차 : 12도
# '감기 조심하세요.'
# 4. 일교차가 11도 미만인 경우 출력 내용
# 일교차 : 9도
# '산책하기 좋은 날씨 입니다.'

'''
여러줄 주석
'''

lowTemp = int(input('최저 기온 : '))
highTemp = int(input('최고 기온 : '))

if lowTemp >= 11:
    print('일교차 : {}도'.format(highTemp - lowTemp))
    print('감기 조심!')
else:
    print('일교차 : {}도'.format(highTemp - lowTemp))
    print('산책하세요!')