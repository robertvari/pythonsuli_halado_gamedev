import pyray as RL
from abc import ABC, abstractmethod
from ResourceManager import ResourceManager

class GameObject(ABC):
    @abstractmethod
    def update(self):
        print("GameObject: update")

    @abstractmethod
    def draw(self):
        print("GameObject: draw")

class Spaceship(GameObject):
    SPEED = 200
    SCALE = 3
    ROTATION = 0
    SOURCE_RECT = (32, 64, 16, 16)
    TEXTURE_NAME = "Ships"

    def __init__(self, resource_manager: ResourceManager):
        print("Spaceship init")
        self._texture = resource_manager.get_texture(self.TEXTURE_NAME)
        self._source_rect = RL.Rectangle(*self.SOURCE_RECT)
        self._size = self._source_rect.width * self.SCALE
        self._origin = RL.Vector2(self._size/2, self._size/2)
        self.position =RL.Vector2(RL.get_screen_width()/2, RL.get_screen_height()/2)

    def draw(self):
        dest_rect = RL.Rectangle(self.position.x, self.position.y, self._size, self._size)
        RL.draw_texture_pro(self._texture, self._source_rect, dest_rect, self._origin, self.ROTATION, RL.WHITE)