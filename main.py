import pyray as RL
from ResourceManager import ResourceManager

class DroneFighter:
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    TITLE = "Drone Fighter"

    def __init__(self):
        RL.init_window(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.TITLE)
        RL.set_target_fps(60)

        self.resources = ResourceManager()
        self.state = "startmenu"

    def update(self):
        if self.state == "startmenu":
            if RL.is_key_pressed(RL.KEY_ENTER):
                self.state = "playing"
        elif self.state == "playing":
            if RL.is_key_pressed(RL.KEY_P):
                self.state = "paused"
        elif self.state == "paused":
            if RL.is_key_pressed(RL.KEY_P):
                self.state = "playing"
        elif self.state == "gameover":
            if RL.is_key_pressed(RL.KEY_ENTER):
                self.state = "startmenu"

    def draw(self):
        RL.begin_drawing()
        RL.clear_background(RL.BLACK)
        RL.draw_texture(self.resources.get_texture("Starfield"), -50, -50, RL.WHITE)

        if self.state == "startmenu":
            RL.draw_text(self.TITLE, 475, 300, 40, RL.WHITE)
            RL.draw_text("Press ENTER to start", 480, 370, 24, RL.LIGHTGRAY)
        elif self.state == "playing":
            RL.draw_text("Playing...", 20, 20, 20, RL.GREEN)
        elif self.state == "paused":
            RL.draw_text("PAUSED", 570, 330, 40, RL.YELLOW)
            RL.draw_text("Press P to resume", 510, 385, 24, RL.LIGHTGRAY)
        elif self.state == "gameover":
            RL.draw_text("GAME OVER", 510, 300, 50, RL.RED)
            RL.draw_text("Press ENTER to return to menu", 430, 370, 24, RL.LIGHTGRAY)

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
