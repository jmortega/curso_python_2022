from dataclasses import dataclass, field

@dataclass
class Computer:
    cpu: str ='CPU'
    freq: int = 0
    price: float = field(init=False, repr=False)
  
computer = Computer(cpu="Intel",freq=3000)
computer.price = 2000
print(computer)  # Computer(cpu='Intel', freq=3000)
print(computer.price)

