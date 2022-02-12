import os
import random

clear = lambda: os.system('cls')


# PLAYER


class Player:
	def __init__(self, game):
		self.game = game
		self.name = "Bruno"

	def play(self):
		
		while True:

			guess = self.game.get_input()

			if len(guess) > 1:
				print("Please only guess ONE letter!")
				continue

			elif len(guess) < 1:
				print('You cannot make an empty guess, silly!')
				continue

			else:
				if type(guess) == int:
					print("Guess a letter, not a number!")
					continue
				else:
					if guess == "q":
						self.game.quit()
					else:
						return guess	


# SCREEN


class Screen:
	def __init__(self, game):
		self.game = game

		self.top_text = str()
		self.bottom_text = str()
		self.board = str()
		self.mantle = []
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

		h = self.body_parts["head"]
		b = self.body_parts["chest"]
		l = self.body_parts["left"]
		r = self.body_parts["right"]

		self.board = f"""
        _________________
        |       |       |
        |       {h}       HANG    
        |      {r}{b}{l}      MAN
        |      {r} {l}      |
       /|\              |
     _/___\_          __|__
		"""

		for letter in self.game.word:
			self.mantle.append("__")

		for space in self.mantle:
			self.bottom_text += space + " "

		self.fullHD_display = f"{self.top_text}\n\n{self.board}\n\n{self.bottom_text}"


# GAME


class Game:
	def __init__(self, word=None):
		self.player = Player(self)
		self.screen = Screen(self)

		self.max_stages = int()
		self.stage = 1
		self.total_rounds = 0
		self.win = False
		self.is_on = False

		self.word = word
		self.remaining_letters = []

	def get_input(self, text=None):

		if text == None:
			x = input()
		else:
			x = input(text)

		if x == "q" or x == "Q" or x == "quit" or x == "Quit":
			self.quit()
		
		return x

	def quit(self):
		self.win = True

	def set_player_name(self):
		self.player.name = self.get_input()
		return self.player.name

	def greet(self):
		
		print("Welcome to Hangman, player! What do I call you?\n\n")
		self.set_player_name()
		print("\n\nGreat name! Shall we begin? [press ENTER to continue. type (q) to QUIT.]\n\n")
		self.get_input()

	def set_word(self, word=None):
		if word == None:
			words = ['cat', 'beach', 'heart', 'meme', 'sky', 'duck']
			self.word = random.choice(words)
		else:
			self.word = word

	def game_setup(self, word=None):
		self.set_word(word)
		self.remaining_letters = list(self.word)
		self.max_stages = len(self.word)
		self.screen.setup()

	def update_screen(self):
		clear()
		print(self.screen.fullHD_display)

	def end_game(self):
		pass

	def check_win(self):
		if len(self.remaining_letters) == 0:
			self.win = True
		elif self.stage == self.max_stages:
			self.end_game()

		if self.win == True:
			self.end_game()

	def game(self):
		self.greet()
		self.game_setup()
		while not self.win:

			self.update_screen()
			x = self.player.play()

			if x in self.remaining_letters:
				i = self.remaining_letters.index(x)
				self.remaining_letters.remove(x)
				self.screen.mantle[i] = x
			

		

	def restart(self):
		pass

# MAIN

game = Game()

game.game()