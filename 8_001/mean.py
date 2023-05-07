import random

nums = random.sample(range(0, 100), 10)
print(f'nums = {nums}')

total = 0
for n in nums:
    total += n

average = total / len(nums)
print(f'average = {average}')

# 50이상 90 이하 수들의 평균
nums = random.sample(range(0, 100), 30)
print(f'nums = {nums}')

targetNums = []
for n in nums:
    if n >= 50 and n <= 90:
        total += n
        targetNums.append(n)

average = total / len(targetNums)
print(f'average = {round(average, 2)}')