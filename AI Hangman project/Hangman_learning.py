import string
import json
import Hangman_engine as engine
import random
from datetime import timedelta
from datetime import datetime
q_table_file = "q_table.json"
q_table = {}
log_file = "log.txt"
states = []
letters = list(string.ascii_uppercase)
letters.append("_")
learning_rate = 0.8
changed_states = set()
for letter1 in letters:
	for letter2 in letters:
		for letter3 in letters:
			for letter4 in letters:
				states.append(letter1+letter2+letter3+letter4)
for state in states:
	q_table[state] = {letter: 0.04 for letter in list(string.ascii_uppercase)}

def playandlearn():
	engine.guesses_allowed = 26
	part_word = engine.start_game(4)
	available_letters = list(string.ascii_uppercase).copy()
	while "_" in part_word:
		entry = q_table[part_word]
		letter = random.choice(available_letters)
		result, part_word = engine.process_guess(letter)
		part_word = part_word.upper()
		score = 0
		if result == engine.Guess_Result.SUCCESS:
			score = 1
		entry[letter] = entry[letter]+learning_rate*(score-entry[letter])
		changed_states.add(part_word)
		available_letters.remove(letter)
report_time = datetime.now()+timedelta(seconds=30)
save_time = datetime.now()+timedelta(minutes=1320)
start_time = datetime.now()
for call in range (0, 10000000):
	playandlearn()
	if len(changed_states) >= 1715:
		print(f"The time taken to reach 1715 states is {datetime.now()-start_time}")
		break
	if datetime.now() > report_time:
		report_time = datetime.now()+timedelta(seconds=30)
		with open(log_file, "a") as log:
			log.write(str(len(changed_states))+"\n")
		print(len(changed_states))
	if datetime.now() > save_time:
		print("Backing up progress to file. Please wait...")
		with open(q_table_file, "w") as json_file:
			json.dump(q_table, json_file)
		with open(log_file, "a") as log:
			log.write("Successfully backed up q_table at "+str(datetime.now()))
		save_time = datetime.now()+timedelta(minutes=1320)
print("Final Saving of file before finishing. Please wait...")
with open(q_table_file, "w") as json_file:
	json.dump(q_table, json_file)
with open(log_file, "a") as log:
	log.write("Finished specified number of calls at "+str(datetime.now()))
input("Finished.")