userName = 'kwon'
userAge = 26

print('User name : {}'.format(userName))
print('User age : {}'.format(userAge))
print('User name : {}, User age : {}'.format(userName, userAge)) # 한 줄에 출력
# {} 안에 index 값을 부여하면 순서를 바꿀 수 있다.
print('User name : {1}, User age : {0}'.format(userName, userAge))

print('나의 이름은 {}이고, 나이는 {}살 입니다. {} 이름은 부모님이 지어 주셨습니다.'.format(userName, userAge, userName))
# index값으로 중복제거
print('나의 이름은 {0}이고, 나이는 {1}살 입니다. {0} 이름은 부모님이 지어 주셨습니다.'.format(userName, userAge))

# 형식 문자를 이용한 데이터 출력
print('User name : %s' % userName)
print('User age : %d' % userAge)
print('User name : %s, User age : %d' % (userName, userAge))