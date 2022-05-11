import random
import Hangman_save as save
import Hangman_engine as engine
import Hangman_config as config

from datetime import datetime, timedelta
algorithm_name = "vowels"
version_number = "0.1"
letters = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
vowels = ["e", "i", "o", "u", "a"]
def play():
	global part_word, result
	if len(engine.guesses) < 5:
		guess = random.choice(vowels)
	else:
		guess = random.choice(letters)
	result, part_word = engine.process_guess(guess)
#	print("Letter: "+guess+"     Result: "+result.name+"     Part word:"+part_word)
stop_time = config.run_time
while datetime.now() < stop_time:
	part_word = engine.start_game()
	result = ""
	
	while "_" in part_word:
		play()
	save.save_game(algorithm_name, version_number, engine.guesses, result.name, engine.chosen_word)
print("Program finished, safe to close.")