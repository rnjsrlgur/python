
# 오름 차순
nums = [5, 10, 2, 1, 0]

for i1 in range(1, len(nums)):
    i2 = i1 - 1
    cNum = nums[i1]

    while nums[i2] > cNum and i2 >= 0:
        nums[i2 + 1] = nums[i2]
        i2 -= 1

    nums[i2 + 1] = cNum

    print(f'nums:{nums}')
print()
print(f'nums:{nums}')
print()

# 내림 차순
nums = [5, 10, 2, 0, 1]
for i1 in range(1, len(nums)):
    i2 = i1 - 1
    cNum = nums[i1]

    while nums[i2] < cNum and i2 >= 0:
        nums[i2 + 1] = nums[i2]
        i2 -= 1

    nums[i2 + 1] = cNum

    print(f'nums:{nums}')
print()
print(f'nums:{nums}')