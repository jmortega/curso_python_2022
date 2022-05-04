class A:
    def __init__(self, name : str):
        self.name = name
        
class B(A):
    def __init__(self, name : str, years : int):
        super().__init__(name)
        self.years = years

class C(B):
    def __init__(self, name : str, years:int):
        super().__init__(name, years)

def main():
    a = A("nameA")
    b = B("nameB", 20)
    c = C("nameC",30)
    print(isinstance(a, A))
    print(isinstance(b, A))
    print(isinstance(c, A))
    
    print(isinstance(a, B))
    print(isinstance(b, B))
    print(isinstance(c, B))
    
    print(isinstance(a, C))
    print(isinstance(b, C))
    print(isinstance(c, C))

main()
