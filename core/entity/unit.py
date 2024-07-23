from .entity import Entity
import random
class Unit (Entity):
    #DNA:list=[23,23,32]
    def __init__(self) -> None:
        super().__init__()
        self.DNA=[23,random.randint(1,40),random.randint(1,40),random.randint(1,40)]
        self.id=random.randint(1,4096)
    def try_mutate(self):
        if random.random()<0.1:
            self.DNA[random.randint(0,len(self.DNA)-1)]=random.randint(1,127)
            print(f"{self.id} mutated!")