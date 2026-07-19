import pyray as RL
from DF_Base import Spaceship

class Player(Spaceship):
    ROTATION = 180

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
