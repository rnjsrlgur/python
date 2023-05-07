def qSort(ns, asc=True):

    if len(ns) < 2:
        return ns

    # 기준값 정하기
    midIdx = len(ns) // 2
    midVal = ns[midIdx]

    smallNums = []; sameNums = []; bigNums = []

    for n in ns:
        if n < midVal:
            smallNums.append(n)

        elif n == midVal:
            sameNums.append(n)

        else:
            bigNums.append(n)

    if asc:
        return qSort(smallNums, asc=asc) + sameNums + qSort(bigNums, asc=asc)
    else:
        return qSort(bigNums, asc=asc) + sameNums + qSort(smallNums, asc=asc)




