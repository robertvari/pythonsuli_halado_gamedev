import pyray as RL


class DroneFighter:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 450
    TITLE = "Drone Fighter"

    # Init game window  
    def __init__(self):
        print("Init window")

        RL.init_window(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.TITLE)
        RL.set_target_fps(60)
    
    # update
    def update(self):
        pass

    # draw
    def draw(self):
        RL.begin_drawing()

        RL.clear_background(RL.BLACK)
        RL.draw_text(self.TITLE, 280, 200, 40, RL.WHITE)

        RL.end_drawing()

    # exit game
    def exit_game(self):
        RL.close_window()
    
    # start game
    def run(self):
        while not RL.window_should_close():
            self.update()
            self.draw()
        self.exit_game()


game = DroneFighter()
game.run()