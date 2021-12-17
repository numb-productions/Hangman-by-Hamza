import os
import random

clear = lambda: os.system('clear')


# PLAYER


class Player:
	def __init__(self, game):
		self.game = game
		self.name = "Default"

	def play(self):
		pass

# SCREEN


class Screen:
	def __init__(self, game):
		self.game = game

		self.top_text = str()
		self.bottom_text = str()
		self.board = str()
		self.mantle = str()
		self.fullHD_display = str()
		self.body_parts = {
			"head": "0",
			"right": "/",
			"left": "\\",
			"chest": "|",
			"empty": " "
		}

	def setup(self):

		self.top_text = f"You have a word made up of {len(self.game.word)} letters."
		self.bottom_text = "Start by guessing a letter"

		h = self.body_parts["head"]
		b = self.body_parts["chest"]
		l = self.body_parts["left"]
		r = self.body_parts["right"]

		self.board = f"""
		_________________
		|		|		|
		|		{h}		HANG
		|	   {r}{b}{l}		MAN
		|	   {r} {l}		|
	   /|\				|
	 _/___\_		  __|__
		"""

		self.fullHD_display = f"{self.top_text}\n\n{self.board}\n\n{self.bottom_text}"


# GAME


class Game:
	def __init__(self, word=None):
		self.player = Player(self)
		self.screen = Screen(self)

		self.stage = 1
		self.total_rounds = 0
		self.win = False
		self.is_on = False

		self.word = word
		self.remaining_letters = 0

	def quit(self):
		pass

	def set_player_name(self):
		self.player.name = input()
		return self.player.name

	def greet(self):
		
		print("welcome to Hangman, player! What do I call you?\n\n")
		b = self.set_player_name()
		print("\n\nGreat name! Shall we begin? [press ENTER to continue. type (q) to QUIT.]\n\n")

		if b == "q" or b == "Q":
			self.quit()

	def set_word(self):
		pass

	def game_setup(self):
		pass

	def update_screen(self):
		pass

	def end_game(self):
		pass

	def check_win(self):
		pass

	def game_loop(self):
		pass

	def restart(self):
		pass

# MAIN

game = Game()