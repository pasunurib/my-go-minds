from abc import ABC,abstractmethod
class A(ABC):
    def m1(self):
        pass
class B(A):
    def m2():
        print("Hello world")

obj=B()
B.m2()
