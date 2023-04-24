# 나와 친구가 좋아하는 번호를 합치되, 번호가 중복되지 않게 하는 프로그램 작성.
# 내 번호 1, 3, 5, 6, 7
# 친구 번호 2, 3, 5, 8, 10

myNums = [1, 3, 5, 6, 7]
frNums = [2, 3, 5, 8, 10]

print('myNums : {}'.format(myNums))
print('frNums : {}'.format(frNums))

addList = myNums + frNums # or myNums.extend(frNums)
print('addList : {}'.format(addList))

result = [] # 빈 리스트 생성
for num in addList:
    if num not in result:
        result.append(num)

print('result : {}'.format(result))