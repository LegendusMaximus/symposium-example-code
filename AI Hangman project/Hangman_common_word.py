
# https://gist.github.com/pozhidaevak/0dca594d6f0de367f232909fe21cdb2f
letter_frequency = {'E': 426, 'T': 313, 'R': 311, 'A': 305, 'I': 298, 'N': 276, 'O': 268, 'S': 225, 'L': 209, 'C': 196, 'P': 136, 'U': 135, 'D': 134, 'H': 116, 'M': 114, 'Y': 96, 'G': 83, 'B': 65, 'F': 65, 'V': 62, 'W': 45, 'K': 36, 'X': 14, 'Q': 9, 'J': 9, 'Z': 3}
import Hangman_save as save
import Hangman_engine as engine
from datetime import datetime, timedelta
import Hangman_config as config
algorithm_name = "common_word"
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