cars = ['그랜저', '소나타', '아반떼', '코나', '베뉴']

# 방법1
n = 0
while n < len(cars):
    print(cars[n])
    n += 1

print()

# 방법2
n = 0
flag = True
while flag:
    print(cars[n])
    n += 1

    if n == len(cars):
        flag = False

print()

# 방법3
n = 0
while True:
    print(cars[n])
    n += 1

    if n == len(cars):
        break