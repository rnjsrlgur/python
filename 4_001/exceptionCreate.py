# 관리자 암호를 입력하고 다음 상태에 따라 예외 처리하는 예외 클래스 만들기.
# 1. 암호 길이가 5미만인 경우:PasswordLengthShortException
# 2. 암호길이가 10초과인 경우:PasswordLengthLongException
# 3. 암호가 잘못된 경우:PasswordWrongException

class PasswordLengthShortException(Exception):
    def __init__(self, str):
        super().__init__(f'{str}: 길이 5미만!')


class PasswordLengthLongException(Exception):
    def __init__(self, str):
        super().__init__(f'{str}: 길이 10초과!')


class PasswordWrongException(Exception):
    def __init__(self, str):
        super().__init__(f'{str}: 잘못된 비밀번호!')


adminPw = input('password : ')

try:
    if len(adminPw) < 5:
        raise PasswordLengthShortException(adminPw)
    elif len(adminPw) > 10:
        raise PasswordLengthLongException(adminPw)
    elif adminPw != 'admin1234':
        raise PasswordWrongException(adminPw)
    elif adminPw == 'adminPw':
        print('빙고!')

except PasswordLengthShortException as e1:
    print(e1)
except PasswordLengthLongException as e2:
    print(e2)
except PasswordWrongException as e3:
    print(e3)