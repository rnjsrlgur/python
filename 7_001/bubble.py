nums = [10, 2, 7, 21, 0]
print(f'not sored nums : {nums}')

length = len(nums) - 1
for i in range(length):
    for j in range(length - i):
        if nums[j] > nums[j + 1]:
            # temp = nums[j]
            # nums[j] = nums[j + 1]
            # nums[j + 1] = temp

            nums[j], nums[j + 1] = nums[j + 1], nums[j]
        print(nums)
    print()

print(f'sorted nums : {nums}')
