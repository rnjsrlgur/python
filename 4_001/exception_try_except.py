# 사용자로부터 숫자 5개를 입력받을 때, 숫자가 아닌 자료형이 입력되면 예외처리

nums = []

n = 1

while n < 6:

    try:
        num = int(input('숫자만 입력 : '))
    except:
        print('예외 발생(숫자만 입력해주세요.)')
        continue

    nums.append(num)
    n += 1

print(f'nums: {nums}')