import pyray as RL
from ResourceManager import ResourceManager
from Player import Player


class DroneFighter:
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    TITLE = "Drone Fighter"

    # Init game window
    def __init__(self):
        print("Init window")

        RL.init_window(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.TITLE)
        RL.set_target_fps(60)

        self.resources = ResourceManager()
        self.player = Player(self.resources)
        self.state = "playing"
    
    # update
    def update(self):
        if self.state == "startmenu":
            pass
        elif self.state == "playing":
            self.player.update()
        elif self.state == "paused":
            pass
        elif self.state == "gameover":
            pass


    # draw
    def draw(self):
        RL.begin_drawing()
        RL.clear_background(RL.BLACK)
        RL.draw_texture(self.resources.get_texture("Starfield"), -50, -50, RL.WHITE)

        if self.state == "startmenu":
            RL.draw_text(self.TITLE, 500, 350, 40, RL.WHITE)
        elif self.state == "playing":
            self.player.draw()
        elif self.state == "paused":
            RL.draw_text("Game Paused", 500, 350, 40, RL.YELLOW)
        elif self.state == "gameover":
            RL.draw_text("Game Over", 500, 350, 40, RL.RED)

        RL.end_drawing()

    # exit game
    def exit_game(self):
        self.resources.unload()
        RL.close_window()
    
    # start game
    def run(self):
        while not RL.window_should_close():
            self.update()
            self.draw()
        self.exit_game()


game = DroneFighter()
game.run()