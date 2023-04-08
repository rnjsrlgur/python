# 연간 누적 강수량 출력
# 1월 30, 2월 45, 3월 47, 4월 55, 5월 65, 6월 100
# 7월 128, 8월 209, 9월 204, 10월 186, 11월 67, 12월 25

total = 0

total += 30
print('1월 누적 강수량 : {}mm'.format(total))

total += 45
print('2월 누적 강수량 : {}mm'.format(total))

total += 47
print('3월 누적 강수량 : {}mm'.format(total))

total += 55
print('4월 누적 강수량 : {}mm'.format(total))

total += 65
print('5월 누적 강수량 : {}mm'.format(total))

total += 100
print('6월 누적 강수량 : {}mm'.format(total))

total += 128
print('7월 누적 강수량 : {}mm'.format(total))

total += 209
print('8월 누적 강수량 : {}mm'.format(total))

total += 204
print('9월 누적 강수량 : {}mm'.format(total))

total += 186
print('10월 누적 강수량 : {}mm'.format(format(total, ',')))

total += 67
print('11월 누적 강수량 : {}mm'.format(format(total, ',')))

total += 25
print('12월 누적 강수량 : {}mm'.format(format(total, ',')))

avg = total / 12
print('-' * 20)
print('연간 누적 강수량 : {}mm'.format(format(total, ',')))
print('평균 강수량 : {}mm'.format(avg))
print('-' * 20)


