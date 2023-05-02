# 새학년이 되어 학급에 20명의 새로운 학생들이 모였다. 학생들을 키 순서대로 줄 세워보자.
# 학생들의 키는 random 모듈을 이용해서 170 ~ 185 사이로 생성한다.

# def bubbleSort(ns): # 얕은 복사
#     length = len(ns) - 1 # 가장 끝에서 바로 앞에 있는 것 까지 비교하기 때문에 -1
#     for i in range(length - 1):
#         for j in range(length - i):
#             if ns[j] > ns[j + 1]:
#                 ns[j], ns[j + 1] = ns[j + 1], ns[j]
#
#     return ns
import copy
def bubbleSort(ns, deepCopy=True):

    if deepCopy:
        cns = copy.copy(ns) # 깊은 복사(원본 데이터 유지)
    else:
        cns = ns # 얕은 복사

    length = len(cns) - 1 # 가장 끝에서 바로 앞에 있는 것 까지 비교하기 때문에 -1
    for i in range(length - 1):
        for j in range(length - i):
            if cns[j] > cns[j + 1]:
                cns[j], cns[j + 1] = cns[j + 1], cns[j]

    return cns