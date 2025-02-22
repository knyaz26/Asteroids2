import pyray as pr

if __name__ == '__main__':
	screen_width = 1280
	screen_height = 720

	pr.init_window(screen_width, screen_height, "asteroids")
	pr.set_target_fps(60)

	while not pr.window_should_close():
		pr.begin_drawing()
		pr.clear_background(pr.BLACK)
		pr.end_drawing()

	pr.close_window()