class TemCls:
    def __init__(self, n, s):
        self.number = n
        self.str = s

    def printClsInfo(self):
        print(f'self.number = {self.number}')
        print(f'self.str = {self.str}')

# 얕은 복사
tc1 = TemCls(10, 'Hello')
tc2 = tc1

tc1.printClsInfo()
tc2.printClsInfo()

print('-' * 50)

tc2.number = 3.14
tc2.str = 'Bye'

tc1.printClsInfo()
tc2.printClsInfo()

print('-' * 50)

# 깊은 복사
import copy

tc3 = TemCls(10, 'Hello')
tc4 = copy.copy(tc3)

tc3.printClsInfo()
tc4.printClsInfo()

print('-' * 50)

# list 복사 copy 이용
scores = [9, 8, 7, 6, 5, 4, 3, 2]
scoresCopy = []

# 얕은 복사
# scoresCopy = scores
# print(f'id(scores) = {id(scores)}')
# print(f'id(scoresCopy) = {id(scoresCopy)}')

# 깊은 복사
# for s in scores:
#     scoresCopy.append(s)
# print(f'id(scores) = {id(scores)}')
# print(f'id(scoresCopy) = {id(scoresCopy)}')

# 다른 깊은 복사 방법
# scoresCopy.extend(scores)
# print(f'id(scores) = {id(scores)}')
# print(f'id(scoresCopy) = {id(scoresCopy)}')

# 다른 깊은 복사 방법
# scoresCopy.copy()
# print(f'id(scores) = {id(scores)}')
# print(f'id(scoresCopy) = {id(scoresCopy)}')

# 다른 깊은 복사 방법
scoresCopy = scores[:]
print(f'id(scores) = {id(scores)}')
print(f'id(scoresCopy) = {id(scoresCopy)}')


