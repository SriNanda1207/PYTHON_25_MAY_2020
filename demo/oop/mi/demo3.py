class A:
    def process(self):
        print("Process in A")


class B(A):
    pass


class C(A):
    def process(self):
        print("Process in C")


class D(B, C):
    pass


print( D.mro())
obj = D()
obj.process()
