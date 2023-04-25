# 개인 정보에 '연락처'와 '주민등록번호'가 있다면 삭제하는 코드 작성.
myInfo = {
    '이름':'gildong',
    '나이':'31',
    '연락처':'010-0000-0000',
    '주민등록번호':'1231554-155455',
    '주소':'경기도 용인시',
}

deleteItem = ['연락처', '주민등록번호']

for i in deleteItem:
    if (i in myInfo):
        del myInfo[i]

print(myInfo)