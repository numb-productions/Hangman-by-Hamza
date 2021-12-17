import os
import random

clear = lambda: os.system('clear')


# PLAYER


class Player:
	def __init__(self, game):
		self.game = game


# SCREEN


class Screen:
	def __init__(self, game):
		self.game = game


# GAME


class Game:
	def __init__(self, word=None):
		self.word = word
		self.player = Player(self)
		self.screen = Screen(self)


# MAIN

game = Game()