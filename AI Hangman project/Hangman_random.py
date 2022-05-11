import random
import Hangman_save as save
import Hangman_engine as engine
from datetime import datetime, timedelta
import Hangman_config	as config


algorithm_name = "random"
version_number = "0.1"
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def play():
	global part_word, result
	guess = random.choice(letters)
	result, part_word = engine.process_guess(guess)
	#print("Letter: "+guess+"     Result: "+result.name+"     Part word:"+part_word)
stop_time = config.run_time
while datetime.now() < stop_time:
	part_word = engine.start_game()
	result = ""
	
	while "_" in part_word:
		play()
	save.save_game(algorithm_name, version_number, engine.guesses, result.name, engine.chosen_word)
print("Program finished, safe to close.")