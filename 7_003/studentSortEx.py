import random
import studentSortMod as sm
import copy

scores = random.sample(range(50, 101), 20)
print(f'scores: {scores}')
print(f'len: {len(scores)}')

print()

print(f'scores: {scores}')
result = sm.sortNum(copy.deepcopy(scores))
print(f'asc: {result}')

print()

print(f'scores: {scores}')
result = sm.sortNum(copy.deepcopy(scores), asc=False)
print(f'desc: {result}')