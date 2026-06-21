import pyray as RL
from ResourceManager import ResourceManager

class Player:
    SPEED = 200
    SCALE = 3

    def __init__(self, resource_manager: ResourceManager):
        self._texture = resource_manager.get_texture("Ships")
        self._source_rect = RL.Rectangle(32, 64, 16, 16)
        self._size = self._source_rect.width * self.SCALE
        self._origin = RL.Vector2(self._size/2, self._size/2)

    def update(self):
        pass

    def draw(self):
        dest_rect = RL.Rectangle(200, 100, self._size, self._size)
        RL.draw_texture_pro(self._texture, self._source_rect, dest_rect, self._origin, 0, RL.WHITE)