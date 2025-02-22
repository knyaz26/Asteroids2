import pyray as pr
from game import Game


if __name__ == '__main__':
	screen_width = 1280
	screen_height = 720
	current_game = Game(screen_width, screen_height)

	pr.init_window(screen_width, screen_height, "asteroids")

	pr.set_target_fps(60)

	current_game.startup()

	while not pr.window_should_close():
		current_game.update()

		pr.begin_drawing()

		current_game.render()

		pr.clear_background(pr.BLACK)

		pr.end_drawing()

	pr.close_window()
	current_game.shutdown()