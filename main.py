import pyray as RL

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450
TITLE = "Drone Fighter"

def main():
    RL.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
    RL.set_target_fps(60)

    while not RL.window_should_close():
        RL.begin_drawing()

        RL.clear_background(RL.BLACK)
        RL.draw_text(TITLE, 280, 200, 40, RL.BLUE)

        RL.end_drawing()

    RL.close_window()


# Start window
main()