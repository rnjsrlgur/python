# 1 ~ 100 난수 10개 생성
# 퀵정렬 알고리즘을 이용한 난수 정렬 모듈 구현
# 오름 차순과 내림차순을 선택할 수 있는 옵션 추가

import random as rd
import quickMod as qm

rNums = rd.sample(range(1, 101), 10)
print(f'not sorted rNums: {rNums}')
print(f'merge sorted rNums ASC: {qm.qSort(rNums)}')
print(f'merge sorted rNums DESC: {qm.qSort(rNums, asc=False)}')