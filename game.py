import pyray as pr
from entity import Entity
from resource_type import ResourceType
import math
import numpy as np
from copy import copy

import random

MAX_METEORS = 15
MAX_SHOTS = 7

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
		if pr.is_key_down(pr.KEY_LEFT):
			self.player.heading -= 5.0
		elif pr.is_key_down(pr.KEY_RIGHT):
			self.player.heading += 5.0
		elif pr.is_key_down(pr.KEY_UP):
			if self.player.acceleration < 1.0:
				self.player.acceleration += 0.03

		self.player.speed.x = math.cos(np.deg2rad(self.player.heading)) * 6.0
		self.player.speed.y = math.sin(np.deg2rad(self.player.heading)) * 6.0

		self.player.position.x += self.player.speed.x * self.player.acceleration
		self.player.position.y += self.player.speed.y * self.player.acceleration

		if self.player.position.x > self.screen_width:
			self.player.position.x = 0.0
		elif self.player.position.x < 0.0:
			self.player.position.x = self.screen_width

		if self.player.position.y > self.screen_height:
			self.player.position.y = 0.0 
		elif self.player.position.y < 0.0:
			self.player.position.y = self.screen_height

		for meteor in self.meteors:
			if meteor.active:
				meteor.position.x += meteor.speed.x * math.cos(np.deg2rad(meteor.heading))
				meteor.position.y += meteor.speed.y * math.sin(np.deg2rad(meteor.heading))

			if meteor.position.x > self.screen_width:
				meteor.position.x = 0.0
			elif meteor.position.x < 0.0:
				meteor.position.x = self.screen_width

			if meteor.position.y > self.screen_height:
				meteor.position.y = 0.0
			elif meteor.position.y < 0.0:
				meteor.position.y = self.screen_height

	def render(self):

		for meteor in self.meteors:
			texture = ResourceType(meteor.type)
			pr.draw_texture_pro(
				self.resources[texture],
				pr.Rectangle(0, 0, self.resources[texture].width, self.resources[texture].height),
				pr.Rectangle(meteor.position.x, meteor.position.y, self.resources[texture].width, self.resources[texture].height),
				pr.Vector2(self.resources[texture].width//2, self.resources[texture].height//2),
				meteor.heading,
				pr.WHITE
				)

		pr.draw_texture_pro(
			self.resources[ResourceType.TEXTURE_PLAYER],
			pr.Rectangle(0, 0, self.resources[ResourceType.TEXTURE_PLAYER].width, self.resources[ResourceType.TEXTURE_PLAYER].height),
			pr.Rectangle(self.player.position.x, self.player.position.y, self.resources[ResourceType.TEXTURE_PLAYER].width//2, self.resources[ResourceType.TEXTURE_PLAYER].height//2),
			pr.Vector2(self.resources[ResourceType.TEXTURE_PLAYER].width//4, self.resources[ResourceType.TEXTURE_PLAYER].height//4),
			self.player.heading,
			pr.WHITE
			)

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
		self.player.active = True
		self.player.speed = pr.Vector2(0, 0)
		self.player.position = pr.Vector2(self.screen_width // 2, self.screen_height // 2)

		for i in range(MAX_METEORS):
			meteor = Entity()
			meteor.active = True 
			meteor.heading = float(pr.get_random_value(0, 360))
			meteor.position = pr.Vector2(float(pr.get_random_value(0, self.screen_width)), float(pr.get_random_value(0, self.screen_height)))
			#meteor.type = pr.get_random_value(self.resources[ResourceType.TEXTURE_METEOR_SMALL], self.resources[ResourceType.TEXTURE_METEOR_LARGE])	
			meteor.speed = pr.Vector2(float(pr.get_random_value(1, 2)), float(pr.get_random_value(1, 2)))
			meteor.type = random.choice([
			    ResourceType.TEXTURE_METEOR_SMALL, 
    			ResourceType.TEXTURE_METEOR_MEDIUM, 
    			ResourceType.TEXTURE_METEOR_LARGE
			])
			self.meteors.append(meteor)


