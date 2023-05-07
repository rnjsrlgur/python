# 재귀 알고리즘을 이용한 최대 공양수 계산
# 유클리드 호제법
# 두 자연수 n1, n2에 대하여(n1 > n2) n1을 n2로 나눈 나머지를 r 이라 할 때,
# n1 n2의 최대공약수는 n2와 r의 최대공약수와 같다.

def gcd(n1, n2):

    if n1 % n2 == 0:
        return n2

    else:
        return gcd(n2, n1 % n2)

print(f'gcd(82, 32): {gcd(82, 32)}')
print(f'gcd(96, 40): {gcd(96, 40)}')
