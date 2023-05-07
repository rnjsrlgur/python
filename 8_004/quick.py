def qSort(ns):

    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2
    midVal = ns[midIdx] # 기준값

    leftNums = []; midNums = []; rightNums = []

    for n in ns:
        if n < midVal:
            leftNums.append(n)
        elif n == midVal:
            midNums.append(n)
        else:
            rightNums.append(n)

    return qSort(leftNums) + midNums + qSort(rightNums)


nums = [8, 1, 4, 3, 2, 5, 4, 10, 6 ,8]
print(f'qSort(nums) : {qSort(nums)}')
