# 사용자가 문자 메세지를 보낼 때 10글자 이하면 SMS로 발송하고, 10글자 초과하면 MMS로 발송하는 프로그램을 예외처리를 이용해서 작성.

def sendSMS(msg):
    if len(msg) > 10:
        raise Exception('길이 초과! MMS로 발송합니다.', 1)

    else:
        print('SMS로 발송합니다.')


def sendMMS(msg):
    if len(msg) <= 10:
        raise Exception('길이 미달! SMS로 발송합니다.', 2)

    else:
        print('MMS로 발송합니다.')

msg = input('메세지를 입력하세요 : ')

try:
    sendSMS(msg)

except Exception as e:
    print(f'e: {e.args[0]}')
    print(f'e: {e.args[1]}')

    if e.args[1] == 1:
        sendMMS(msg)
    elif e.args[1] == 2:
        sendSMS(msg)