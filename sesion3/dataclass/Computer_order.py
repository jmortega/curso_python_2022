from dataclasses import dataclass

@dataclass(order=True)
class Computer:
    cpu: str ='CPU'
    freq: int = 0
    price: int = 0
    
    def __str__(self) -> str:
    	return f'{self.cpu}: {self.freq}, {self.price}'

computer = Computer(freq=3000,price=2000)
computer2 = Computer(freq=2000,price=1500)
 
print(computer>=computer2)  # True
