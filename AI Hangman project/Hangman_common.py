
# https://gist.github.com/pozhidaevak/0dca594d6f0de367f232909fe21cdb2f
letter_frequency = {'E' : 12.0,
    'T' : 9.10,
    'A' : 8.12,
    'O' : 7.68,
    'I' : 7.31,
    'N' : 6.95,
    'S' : 6.28,
    'R' : 6.02,
    'H' : 5.92,
    'D' : 4.32,
    'L' : 3.98,
    'U' : 2.88,
    'C' : 2.71,
    'M' : 2.61,
    'F' : 2.30,
    'Y' : 2.11,
    'W' : 2.09,
    'G' : 2.03,
    'P' : 1.82,
    'B' : 1.49,
    'V' : 1.11,
    'K' : 0.69,
    'X' : 0.17,
    'Q' : 0.11,
    'J' : 0.10,
    'Z' : 0.07 }
import Hangman_save as save
import Hangman_engine as engine
import Hangman_config as config
from datetime import datetime, timedelta
algorithm_name = "common"
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