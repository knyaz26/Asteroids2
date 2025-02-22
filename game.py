import pyray as pr

class Game:
	def __init__(self, screen_width, screen_height):
		#json for all the assets.
		self.resources = {}
		#arrays for objects.
		self.meteors = []
		self.shots = []
		#variables.
		self.screen_width = screen_width
		self.screen_height = screen_height

	def startup(self):
		pass

	def update(self):
		pass

	def render(self):
		pass

	def shutdown(self):
		pass