import pyray as pr
from entity import Entity
from resource_type import ResourceType

class Game:
	def __init__(self, screen_width, screen_height):
		#json for all the assets.
		self.resources = {}
		#arrays for objects.
		self.meteors = []
		self.shots = []
		#variables.
		self.player = Entity()
		self.screen_width = screen_width
		self.screen_height = screen_height

	def startup(self):
		pr.init_audio_device()

		image = pr.load_image("assets/sprite-0004.png")
		self.resources[ResourceType.TEXTURE_METEOR_SMALL] = pr.load_texture_from_image(image)
		pr.unload_image(image)

		image = pr.load_image("assets/sprite-0003.png")
		self.resources[ResourceType.TEXTURE_METEOR_MEDIUM] = pr.load_texture_from_image(image)
		pr.unload_image(image)

		image = pr.load_image("assets/sprite-0002.png")
		self.resources[ResourceType.TEXTURE_METEOR_LARGE] = pr.load_texture_from_image(image)
		pr.unload_image(image)

		image = pr.load_image("assets/sprite-0001.png")
		self.resources[ResourceType.TEXTURE_PLAYER] = pr.load_texture_from_image(image)
		pr.unload_image(image)

		self.resources[ResourceType.SOUND_LAZER_SHOOT] = pr.load_sound("assets/audio-0001.mp3")
		self.resources[ResourceType.SOUND_LAZER_EXPLOSION] = pr.load_sound("assets/audio-0002.mp3")

		self.reset()

	def update(self):
		pass

	def render(self):
		pass

	def shutdown(self):
		pr.unload_texture(self.resources[ResourceType.TEXTURE_METEOR_SMALL])
		pr.unload_texture(self.resources[ResourceType.TEXTURE_METEOR_MEDIUM])
		pr.unload_texture(self.resources[ResourceType.TEXTURE_METEOR_LARGE])
		pr.unload_texture(self.resources[ResourceType.TEXTURE_PLAYER])

		pr.unload_sound(self.resources[ResourceType.SOUND_LAZER_SHOOT])
		pr.unload_sound(self.resources[ResourceType.SOUND_LAZER_EXPLOSION])
		pr.close_audio_device()

	def reset(self):
		self.shots.clear()
		self.meteors.clear()

		#player settings when game is reset.
		self.player.heading = 0.00
		self.player.acceleration = 0.00
		self.player.active = true
		self.player.speed = pr.Vector2(0, 0)
		self.player.position = pr.Vector2(self.screen_width // 2, self.screen_height // 2)




