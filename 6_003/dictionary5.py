memInfo = {
    '이름':'홍길동',
    '메일':'dsad@naver.com',
    '학년':3,
    '취미':['게임', '야구']
}
print(f'memInfo: {memInfo}')

del memInfo['메일']
print(f'memInfo: {memInfo}')

del memInfo['취미']
print(f'memInfo: {memInfo}')

# pop()과 key를 이용한 아이템 삭제
memInfo = {
    '이름':'홍길동',
    '메일':'dsad@naver.com',
    '학년':3,
    '취미':['게임', '야구']
}
print(f'memInfo: {memInfo}')

returnVal = memInfo.pop('이름')
print(f'memInfo: {memInfo}')