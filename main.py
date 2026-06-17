import pyray as RL
from ResourceManager import ResourceManager

class DroneFighter:
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    TITLE = "Drone Fighter"

    def __init__(self):
        # Initialize Raylib window
        RL.init_window(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.TITLE)
        RL.set_target_fps(60)

        self.resources = ResourceManager()

    def update(self):
        # Updates game state
        pass

    def draw(self):
        # Draw game
        RL.begin_drawing()
        RL.clear_background(RL.BLACK)
        RL.draw_texture(self.resources.get_texture("Starfield"), -50, -50, RL.WHITE)
        RL.draw_text(self.TITLE, 500, 350, 40, RL.WHITE)
        RL.end_drawing()

    def exit_game(self):
        self.resources.unload()
        RL.close_window()

    def run(self):
        # Start game
        while not RL.window_should_close():
            self.update()
            self.draw()
        self.exit_game()


game = DroneFighter()
game.run()
