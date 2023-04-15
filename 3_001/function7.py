# 사용자가 길이(cm)를 입력하면 mm로 환산한 값을 반환하는 함수 만들기
def cmToMm(cm):
    result = cm * 10
    return result

length = float(input('길이(cm) : '))
returnVal = cmToMm(length)
print(f'returnVal: {returnVal}mm')