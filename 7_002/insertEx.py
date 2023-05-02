import random
import insertMod as sm

nums = random.sample(range(1, 1000), 100)
print(f'not sorted nums : {nums}')

#
sn = sm.sortNums(nums)

# asc
sn.setSort()
sortedNums = sn.getSortedNums()
print(f'sorted Nums by ASC : {sortedNums}')

# desc
sn.isAscending(False)
sn.setSort()
sortedNums = sn.getSortedNums()
print(f'sorted Nums by DESC : {sortedNums}')

# min & max
print(f'min num : {sn.getMinNum()}')
print(f'max num : {sn.getMaxNum()}')