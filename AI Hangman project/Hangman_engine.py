import random
from enum import Enum
class Guess_Result(Enum):
	SUCCESS = 1
	FAILURE = 2
	DUPLICATE = 3
	GAME_OVER = 4



guesses = []
chosen_word = "" 
part_word = ""
words = []
guesses_allowed = 15
guesses_left = -1


def _load_words():
	words_file = open("common.txt")
	for line in words_file:
		word = line.strip()
		words.append(word)
 


def _choose_word(word_len):
	global chosen_word
	if word_len == 0:
		chosen_word = random.choice(words)
	else:
		stripped_words = []
		for word in words:
			if len(word) == word_len:
				stripped_words.append(word)
		chosen_word = random.choice(stripped_words)
	chosen_word = chosen_word.lower()


def _create_part_word():
	global part_word 
	part_word = ""
	for letter in list(chosen_word):
		if letter in guesses:
			part_word = part_word+letter
		else:
			part_word = part_word+"_"
	return part_word


def process_guess(guess):
	global guesses_left, chosen_word
	guess = guess.strip()
	guess = guess.lower()
	guess = guess[0]
	if guesses_left <= 0:
		return Guess_Result.GAME_OVER, chosen_word
	if guess in guesses:
		return Guess_Result.DUPLICATE, _create_part_word()
	guesses.append(guess)
	if guess in chosen_word:
		return Guess_Result.SUCCESS, _create_part_word()
	guesses_left = guesses_left - 1
	return Guess_Result.FAILURE, _create_part_word()


def num_wrong_guesses():
	wrong_guesses = 0
	for guess in guesses:
		if guess not in chosen_word:
			wrong_guesses += 1
	return wrong_guesses

def start_game(word_len=0):
	if len(words) == 0:
		_load_words()
	_choose_word(word_len)
	global guesses 
	guesses = []
	global guesses_left 
	guesses_left = guesses_allowed
	return _create_part_word()
