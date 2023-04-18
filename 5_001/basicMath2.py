# 사용자가 입력한 수를 소인수 분해

userInput = int(input("1보다 큰 정수 입력 : "))

n = 2
searchNum = []
while n <= userInput:
    if userInput % n == 0:
        print('소인수 : {}'.format(n))
        if searchNum.count(n) == 0:
            searchNum.append(n)
        elif searchNum.count(n) == 1:
            searchNum.remove(n)
        userInput /= n
    else:
        n += 1

print(searchNum)