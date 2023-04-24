# 특정 위치에 아이템 추가
nums = [1, 3, 6, 11, 45, 54, 62, 74, 85]
inputNum = int(input('num : '))
insertIdx = 0

for idx, num in enumerate(nums):
    print(idx, num)

    if insertIdx == 0 and inputNum < num:
        insertIdx = idx

nums.insert(insertIdx, inputNum)
print(nums)