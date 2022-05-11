
letter_frequency = {'E': 108, 'A': 95, 'L': 61, 'O': 61, 'T': 60, 'R': 55, 'N': 55, 'I': 53, 'S': 53, 'D': 42, 'H': 34, 'P': 33, 'M': 29, 'C': 28, 'U': 28, 'W': 26, 'K': 26, 'F': 26, 'B': 24, 'Y': 21, 'G': 17, 'V': 8, 'J': 5, 'Z': 1}
import Hangman_save as save
import Hangman_engine as engine
import Hangman_config as config	
from datetime import datetime, timedelta
algorithm_name = "common_word_4"
version_number = "0.1"
letters = []
def play():
	global part_word, result
	guess = letters[0]
	del letters[0]
	result, part_word = engine.process_guess(guess)
	#print("Letter: "+guess+"     Result: "+result.name+"     Part word:"+part_word)
stop_time = config.run_time
while datetime.now() < stop_time:
	letters = list(letter_frequency.keys()).copy()
	part_word = engine.start_game()
	result = ""
	
	while "_" in part_word:
		play()
	save.save_game(algorithm_name, version_number, engine.guesses, result.name, engine.chosen_word)
print("Program finished, safe to close.")