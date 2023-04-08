# 자동차 배기량에 따라 세금을 부과한다. 배기량을 입력하면 세금이 출력되는 프로그램 작성.

car = int(input("배기량 입력 : "))

if car < 1000:
    print("세금 : 100,000원")
elif car >= 1000 and car < 2000:
    print("세금 : 200,000원")
elif car >= 2000 and car < 3000:
    print("세금 : 300,000원")
elif car >= 3000 and car < 4000:
    print("세금 : 400,000원")
elif car >= 4000 and car < 5000:
    print("세금 : 500,000원")
elif car >= 5000:
    print("세금 : 600,000원")