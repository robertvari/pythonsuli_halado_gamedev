import pyray as RL
from DF_Base import Spaceship

class Player(Spaceship):
    ROTATION = -90
    TAG = "player"

    def update(self, dt: float):
        # Move spaceship
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

        self.move(RL.Vector2(dx, dy), dt)
        self.rotate_to(RL.get_mouse_position())

        if RL.is_mouse_button_pressed(RL.MouseButton.MOUSE_BUTTON_LEFT):
            self.shoot(RL.vector2_subtract(RL.get_mouse_position(), self.position))