import pyray as RL
from ResourceManager import ResourceManager


class Player:
    SPEED = 200
    SCALE = 3

    def __init__(self, resource_manager: ResourceManager):
        self._texture = resource_manager.get_texture("Ships")
        self._source_rect = RL.Rectangle(32, 64, 16, 16)
        cx = RL.get_screen_width() / 2
        cy = RL.get_screen_height() / 2
        self.position = RL.Vector2(cx, cy)

    def update(self):
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
        size = self._source_rect.width * self.SCALE
        dest = RL.Rectangle(self.position.x, self.position.y, size, size)
        origin = RL.Vector2(size / 2, size / 2)
        RL.draw_texture_pro(self._texture, self._source_rect, dest, origin, 180.0, RL.WHITE)
