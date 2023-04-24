# 다음은 전쟁에서 사용되는 암호이다. 암호를 해독하는 프로그램 작성
# 암호 : '27156231'
# 해독 : '13326125157214'

secret = '27156231'
secretList = []
solvedList = ''

for char in secret:
    secretList.append(int(char))

secretList.reverse()
print(secretList)

val = secretList[0] * secretList[1]
secretList.insert(2, val)
print(secretList)

val = secretList[3] * secretList[4]
secretList.insert(5, val)
print(secretList)

val = secretList[6] * secretList[7]
secretList.insert(8, val)
print(secretList)

val = secretList[9] * secretList[10]
secretList.insert(11, val)
print(secretList)