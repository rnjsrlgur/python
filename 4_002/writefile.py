import time

lt = time.localtime()

# dateStr = '[' + str(lt.tm_year) + '년' + str(lt.tm_mon) + '월' + str(lt.tm_mon) + '일]'
dateStr = '[' + time.strftime('%Y년 %m월 %d일 %H:%M:%S %p') + ']'
f = open('C:/pythonEx/pythonTxt/test.txt', 'w')

todaySchedule = input('오늘 일정 : ')
f.write(dateStr + todaySchedule)
f.close()