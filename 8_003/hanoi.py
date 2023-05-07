# 하노이탑
# 제약조건
# 1. 한 번에 한개의 원판만 옮길 수 있다.
# 2. 큰 원판이 작은 원판 위에 있어서는 안된다.

        # 원판개수, 시작기둥, 도착기둥, 경유기둥
def hanoi(discCnt, frontBar, toBar, viaBar):
    if discCnt == 1:
        print(f'{discCnt}disc: {frontBar}에서 {toBar}로 이동!')

    else:
        # (disc-1)개들을 경유 기둥으로 이동
        hanoi(discCnt - 1, frontBar, viaBar, toBar)
        # discCnt를 목적 기둥으로 이동
        print(f'{discCnt}disc: {frontBar}에서 {toBar}로 이동!')
        # (disc-1)개들을 도착 기둥으로 이동
        hanoi(discCnt - 1, viaBar, toBar, frontBar)

hanoi(3, 1, 3, 2)
print()
hanoi(4, 1, 3, 2)