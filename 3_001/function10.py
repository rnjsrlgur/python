# 삼각형, 사각형, 원의 넓이를 반환하는 lambda 함수 만들기.
getTriangleArea = lambda n1, n2: (n1 * n2 / 2)
getSquareArea = lambda n1, n2: n1 * n2
getCircleArea = lambda r: r * r * 3.14

width = int(input('가로 : '))
height = int(input('세로 : '))
radius = int(input('반지름 : '))

triangleVal = getTriangleArea(width, height)
squareVal = getSquareArea(width, height)
circleVal = getCircleArea(radius)

print(f'삼각형 넓이 : {triangleVal}')
print(f'사각형 넓이 : {squareVal}')
print(f'원 넓이 : {circleVal}')