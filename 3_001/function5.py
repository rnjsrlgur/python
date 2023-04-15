def printNum(*numbers):
    for number in numbers:
        print(number, end='')
    print()

printNum()
printNum(1)
printNum(1, 2)
printNum(1, 2, 3)