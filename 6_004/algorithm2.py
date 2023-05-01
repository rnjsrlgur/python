nums = [4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9]

searchData = int(input('search num : '))
searchResultIdx = -1
# 리스트에서 가장 앞에 있는 숫자 '7'을 검색하고, 위치 출력
nums.append(searchData)


n = 0
while True:
    if nums[n] == searchData:
        if n != len(nums) - 1:
            searchResultIdx = n
        break

    n += 1

print(f'nums: {nums}')
print(f'nums Length: {len(nums)}')
print(f'searchResultIdx: {searchResultIdx}')

if searchResultIdx < 0:
    print('not search index')
else:
    print(f'searchResultIdx: {searchResultIdx}')

# 리스트에서 숫자 '7'을 모두 검색하고 각각의 위치와 검색 개수 출력

searchResultIdxs = []

nums.append(searchData)

n = 0
while True:
    if nums[n] == searchData:
        if n != len(nums) - 1:
            searchResultIdxs.append(n)
        else:
            break

    n += 1

print(f'nums: {nums}')
print(f'nums Length: {len(nums)}')
print(f'searchResultIdxs: {searchResultIdxs}')
print(f'searchResultCnts: {len(searchResultIdxs)}')