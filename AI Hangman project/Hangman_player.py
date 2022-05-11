import Hangman_engine as engine
from Hangman_engine import Guess_Result
import Hangman_save as save
name = input("Please enter your name.")
algorithm_name = "player_"+name
version_number = 0.1


def play():
	part_word = engine.start_game()
	while "_" in part_word:
		print(f"Guess this word: {space_part_word(part_word)}")
		guess = input("Type your guess here...")
		result, part_word = engine.process_guess(guess)
		print(print_result(result))
		if result == Guess_Result.GAME_OVER:
			break
	if result == Guess_Result.SUCCESS:
		print(f"Well done. You won with {engine.guesses_left} more wrong guesses left. The word was ", engine.chosen_word)
	save.save_game(algorithm_name, version_number, engine.guesses, result.name, engine.chosen_word)

def space_part_word(part_word):
	result = ""
	for letter in part_word:
		result += letter+" "
	result = result.strip()
	return result

def print_result(result):
	output = "No result"
	if result == Guess_Result.SUCCESS:
		output = "Well done! Your guess was correct."
	elif result == Guess_Result.FAILURE:
		output = f"Boo! Your guess was not in the word. Have another try. You are allowed {engine.guesses_left} more wrong guesses before you are hanged."
	elif result == Guess_Result.DUPLICATE:
		output = "You have already guessed this! Try something else."
	elif result == Guess_Result.GAME_OVER:
		output = f"Sorry, you have reached your guesses limit (which was {engine.guesses_allowed}) and you have been hanged. Why not play again? The word you were trying to guess was {engine.chosen_word}"
	return output		
play()