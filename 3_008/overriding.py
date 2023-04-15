# 삼각형의 넓이를 계산하는 클래스를 만들고,
# 이를 상속하는 클래스에서 getArea()를 오버라이딩 해서
# 출력

class TArea:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def printTArea(self):
        print(f'width: {self.width}')
        print(f'height: {self.height}')

    def getArea(self):
        return self.width * self.height / 2

class newTArea(TArea):
    def __init__(self, w, h):
        super().__init__(w, h)

    def getArea(self):
        return str(super().getArea()) + '㎠'

ta = newTArea(7, 5)
ta.printTArea()
taArea = ta.getArea()
print(f'taArea: {taArea}')