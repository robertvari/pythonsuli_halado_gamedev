import pyray as RL

class DroneFighter:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 450
    TITLE = "Drone Fighter"

    def __init__(self):
        # Initialize Raylib window
        RL.init_window(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.TITLE)
        RL.set_target_fps(60)

    def update(self):
        # Updates game state
        pass

    def draw(self):
        # Draw game
        RL.begin_drawing()
        RL.clear_background(RL.BLACK)
        RL.draw_text(self.TITLE, 280, 200, 40, RL.BLUE)
        RL.end_drawing()

    def exit_game(self):
        # Cleans up and exits game
        RL.close_window()

    def run(self):
        # Start game
        while not RL.window_should_close():
            self.update()
            self.draw()
        self.exit_game()


game = DroneFighter()
game.run()
