# 리스트를 오름차순으로 정렬한 후, '7'을 검색하고 인덱스 반환

nums = [4, 10, 22, 5, 0, 17, 7, 11, 9, 61, 88]

nums.sort()

searchData = int(input('찾으려는 숫자 : '))
searchResultIdx = -1

startIdx = 0
endIdx = len(nums) - 1
midIdx = (startIdx + endIdx) // 2
midVal = nums[midIdx]


while searchData <= nums[len(nums) - 1] and searchData >= nums[0]:

    if searchData == nums[len(nums) - 1]:
        searchResultIdx = len(nums) - 1
        break

    if searchData > midVal:
        startIdx = midIdx
        midIdx = (startIdx + endIdx) // 2
        midVal = nums[midIdx]
        print(f'midIdx : {midIdx}')
        print(f'midVal : {midVal}')

    elif searchData < midVal:
        endIdx = midIdx
        midIdx = (startIdx + endIdx) // 2
        midVal = nums[midIdx]
        print(f'midIdx : {midIdx}')
        print(f'midVal : {midVal}')

    elif searchData == midVal:
        searchResultIdx = midIdx
        break

print(f'searchResultIdx : {searchResultIdx}')