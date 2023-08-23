from abc import ABC,abstractmethod
@abstractmethod
class A(ABC):
    pass

class B(A):
    def m1():
        print(" TEA--SHOP  ")
        print("------------")
        print("items price qnt Amt")
        sub=["Tea   ","Coffee","Boast "]
        price=[10,15,20]
        QNT=[0  ,1  ,  2]
        for i in range(3):
            print(sub[i]," ",price[i],   QNT[i])
    def m2(self):
        pass
class C(B):
    def m1(self):
        price=[10,15,20]

        Amt=sum(price)

        print("------------")
        print("Amt    =",  Amt )
        print("------------")
ob=B()
B.m1()
ab=C()
ab.m1()

