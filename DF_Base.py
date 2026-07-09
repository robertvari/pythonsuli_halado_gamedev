from abc import ABC, abstractmethod

class GameObject(ABC):
    @abstractmethod
    def update(self):
        print("GameObject: update")

    @abstractmethod
    def draw(self):
        print("GameObject: draw")
