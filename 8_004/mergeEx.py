# 1 ~ 100까지의 난수 10개를 생성하고, 요구 사항을 만족하는 모듈 생성.
# 1. 병합정렬 알고리즘을 이용한 난수 정렬 모듈 구현.
# 2. 위의 모듈에 오름차순과 내림차순을 선택할 수 있는 옵션 추가.

import random as rd
import mergeSortMod as sm

nums = rd.sample(range(1, 101), 10)
print(f'not sorted nums: {nums}')
print(f'sorted nums ASC : {sm.mSort(nums)}')
print(f'sorted nums DESC : {sm.mSort(nums, asc=False)}')