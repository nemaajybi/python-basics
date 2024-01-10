class A:
    def do(self):
        print('in A')

class B(A):
    pass

class c:
    def do(self):
        print('in c')

class D(C,B):
    pass
j= D()
j.do()
