import os
import random

clear = lambda: os.system('clear')


# WORD


class Word:
	def __init__(self, game):
		self.game = game
		self.word = ""
		self.words = ["cat", "dog", "bird", "red", "magenta"]
		self.fill = "__"

	def choose_word(self):
		self.word = random.choice(self.words)
		self.game.remaining_letters = list(self.word)
		self.game.bottom = [self.fill * len(self.word)]


# PLAYER


class Player:
	def __init__(self, game):
		self.game = game

	def play(self):
		char = input("Guess a letter, boi: ")
		for letter in self.game.word.word:
			if char == self.game.word.word:
				self.game.remaining_letters[letter - 1] = "$"
				self.game.bottom[letter - 1] = char


# SCREEN


class Screen:
	def __init__(self, game):
		self.parts = ["0", "\\", "/", "|"]

		self.board = f"""
	_________
	|		|
	|		{self.parts[0]}
	|	   {self.parts[2]}{self.parts[4]}{self.parts[1]}
	|	   {self.parts[2]} {self.parts[1]}
	|
  __|__
		"""

		self.display = f"""
{self.top}

{self.board}

{self.bottom}
		"""


# GAME


class Game:
	def __init__(self):
		self.player = Player()
		self.word = Word()
		self.screen = Screen()
		self.remaining_letters = []

	def update(self):
		clear()
		print(self.screen.display)

	def play(self):
		pass


# MAIN

game = Game()
game.play()