from abc import ABCMeta, abstractmethod


class Airplane(metaclass=ABCMeta):
    @abstractmethod
    def flight(self):
        pass

    def forward(self):
        print('전진!')

    def backward(self):
        print('후진!')

class Airline(Airplane):

    def __init__(self, c):
        self.color = c

    def flight(self):
        print('이륙!')

al = Airline('red')
al.flight()
al.forward()
al.backward()
