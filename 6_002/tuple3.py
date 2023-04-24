# 나와 친구가 좋아하는 번호를 합치되, 번호가 중복되지 않게 하는 프로그램 작성
myNums = (1, 3, 5, 6, 7)
frNums = (2, 3, 5, 8, 10)

print('myNums : {}'.format(myNums))
print('frNums : {}'.format(frNums))

for num in frNums:
    if num not in myNums:
        myNums = myNums + (num,)

print('result : {}'.format(myNums))