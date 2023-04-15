class Robot:
    def __init__(self, color, height, weight):
        self.color = color
        self.height = height
        self.weight = weight

    def printRobotInfo(self):
        print(f"Color: {self.color}")
        print(f"Height: {self.height}")
        print(f"Weight: {self.weight}")

rb1 = Robot("Red", 100, 100)
rb1.printRobotInfo()
rb2 = Robot("Blue", 200, 200)
rb2.printRobotInfo()
rb3 = rb1 # 얕은 복사 # 객체가 복사되는게 아니라, 주소값이 복사됨.
rb3.printRobotInfo()