class A:
    def __init__(self, A):
        print("Empieza A")
        self.A = A
        print("Finaliza A")
        
class B(A):
    def __init__(self, A, B):
        print("Empieza B")
        super().__init__(A)
        print("Finaliza B")
        
class C(B):
    def __init__(self, A, B , C):
        print("Empieza C")
        super().__init__(A, B)
        print("Finaliza C")
        
class D(C):
    def __init__(self, A, B, C, D):
        print("Empieza D")
        super().__init__(A, B, C)
        print("Finaliza D")
        
D(1,2,3,4)