from dataclasses import dataclass

@dataclass
class Computer:
    cpu: str
    freq: int
    price: int = 1000

    def discount(self):
        return self.price*0.8
    
    def __str__(self) -> str:
    	return f'{self.cpu}: {self.freq}, {self.price}'

computer = Computer("Intel Core i7",4000,2000)
print(computer.discount())
print(computer)
computer = str(computer)  
print(computer)  # Intel Core i7: 4000, 2000
