import pyray as RL
from abc import ABC, abstractmethod
from ResourceManager import ResourceManager

class GameObject(ABC):
    @abstractmethod
    def update(self, dt: float):
        print("GameObject: update")

    @abstractmethod
    def draw(self):
        print("GameObject: draw")

class Spaceship(GameObject):
    SPEED = 200
    ACCELERATION = 400
    DECELERATION = 100
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
        self.velocity = RL.Vector2(0, 0)
    
    def move(self, direction: RL.Vector2, dt: float):
        if direction.x != 0 or direction.y != 0:
            direction = RL.vector2_normalize(direction)
            target_velocity = RL.vector2_scale(direction, self.SPEED)
            rate = self.ACCELERATION
        else:
            target_velocity = RL.Vector2(0, 0)
            rate = self.DECELERATION

        self.velocity = RL.vector2_move_towards(self.velocity, target_velocity, rate * dt)
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

    def draw(self):
        dest_rect = RL.Rectangle(self.position.x, self.position.y, self._size, self._size)
        RL.draw_texture_pro(self._texture, self._source_rect, dest_rect, self._origin, self.ROTATION, RL.WHITE)
