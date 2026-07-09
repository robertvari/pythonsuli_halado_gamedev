import pyray as RL
from DF_Base import GameObject
from ResourceManager import ResourceManager
from DF_Base import GameObject

class Player(GameObject):
    SPEED = 200
    SCALE = 3

    def __init__(self, resource_manager: ResourceManager):
        self._texture = resource_manager.get_texture("Ships")
        self._source_rect = RL.Rectangle(32, 64, 16, 16)
        self._size = self._source_rect.width * self.SCALE
        self._origin = RL.Vector2(self._size/2, self._size/2)
        self.position =RL.Vector2(RL.get_screen_width()/2, RL.get_screen_height()/2)

    def update(self):
        # Move spaceship
        dt = RL.get_frame_time()
        dx = 0
        dy = 0

        if RL.is_key_down(RL.KeyboardKey.KEY_W):
            dy -= 1
        if RL.is_key_down(RL.KeyboardKey.KEY_S):
            dy += 1
        if RL.is_key_down(RL.KeyboardKey.KEY_A):
            dx -= 1
        if RL.is_key_down(RL.KeyboardKey.KEY_D):
            dx += 1

        direction = RL.vector2_normalize(RL.Vector2(dx, dy))
        self.position.x += direction.x * self.SPEED * dt
        self.position.y += direction.y * self.SPEED * dt

    def draw(self):
        dest_rect = RL.Rectangle(self.position.x, self.position.y, self._size, self._size)
        RL.draw_texture_pro(self._texture, self._source_rect, dest_rect, self._origin, 180, RL.WHITE)