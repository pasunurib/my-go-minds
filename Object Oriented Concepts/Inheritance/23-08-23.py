from abc import ABC,abstractmethod
@abstractmethod
class A(ABC):
    pass

class B(A):
    def m1():
        print("Helloworld")
    def m2(self):
        pass
class C(B):
    def m2(self):
        print("My name is Bhanu")


ob=B()
B.m1()
ab=C()
ab.m2()





