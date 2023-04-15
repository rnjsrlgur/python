class Car:  # 클래스 선언
    def __init__(self, color, length):  # 생성자, 속성
        self.color = color
        self.length = length
    def doStop(self):  # 기능
        print('STOP!')
    def doStart(self):  # 기능
        print('START!')

car1 = Car('red', 200)
car2 = Car('blue', 300)