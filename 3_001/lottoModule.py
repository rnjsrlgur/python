# 로또 번호를 출력하는 모듈 만들기
import random
def getLottoNum():
    result = random.sample(range(1, 46), 6)

    return result