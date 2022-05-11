from datetime import datetime
from Hangman_engine import Guess_Result
from datetime import timedelta
import json
import Hangman_engine as engine
import Hangman_save as save

algorithm_name = "learning_play"
version_number = 0.1


def load_q_table():
	with open ("q_table.json", "r") as q_table_file:
		return json.load(q_table_file)

def play(q_table):
	part_word = engine.start_game(4)
	guesses = []
	result = Guess_Result.DUPLICATE
	while "_" in part_word and result != Guess_Result.GAME_OVER:
		scores = dict(q_table[part_word])
		#print(scores)
		for guess in guesses:
			scores.pop(guess, None)
		high_score = -1
		high_letter = "!"
		for key in scores:
			if scores[key] > high_score:
				high_score = scores[key]
				high_letter = key
		result, part_word = engine.process_guess(high_letter)
		part_word = part_word.upper()
		guesses.append(high_letter)
	return result
			

def main():
	q_table = load_q_table()
	print(f"Length of Q table is {len(q_table.keys())}. Q table has loaded successfully.")
	#print(search_keys(q_table))
	stop_time = datetime.now()+timedelta(days=7)
	while datetime.now() <= stop_time:
		result = play(q_table)
		#print(f"{result} Saving game...")
		save.save_game(algorithm_name, version_number, engine.guesses, result.name, engine.chosen_word)
		#print("Game saved to file")


def search_keys(q_table):
	found_keys = []
	for key in q_table.keys():
		if "l" in key and "_" in key:
			found_keys.append(key)
	return found_keys

if __name__ == "__main__":
	main()
print("This algorithm has finished and games are saved.")