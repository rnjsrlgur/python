datas = [3, 2, 5, 7, 9, 1, 0, 8, 6, 4]
print(f'data: {datas}')
print(f'data length: {len(datas)}')

searchData = int(input('찾으려는 숫자 데이터 입력 : '))
searchResultIdx = -1

n = 0
while True:
    if n == len(datas):
        searchResultIdx = -1
        break
    elif datas[n] == searchData:
        searchResultIdx = n
        break
    n += 1

print(f'searchResultIdx: [{searchResultIdx}]')