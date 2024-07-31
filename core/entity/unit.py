from typing import Callable
from .entity import Entity
import random


class Unit(Entity):
    #called in scheduler.next, controlling unit's action
    act: Callable

    def __init__(self, act,**args) -> None:
        super().__init__()
        self.id = random.randint(1, 4096) if "id" not in args else args["id"]
        self.act = act

    def try_mutate(self):
        """
        to change the logic of unit
        """
        if random.random() < 0.1:
            self.DNA[random.randint(0, len(self.DNA) - 1)] = random.randint(1, 127)
            print(f"{self.id} mutated!")
