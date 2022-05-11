import csv
import os
from datetime import datetime
filename = "games.csv"
def save_game(algorithm_name, version_number, guesses, result, chosen_word):
	if not os.path.isfile(filename):
		with open(filename, "w") as file:
			file.write("Algorithm name,Version number,Time,Result,Chosen word,Guesses\n")
	with open(filename, "a") as file:
		row = f"{algorithm_name},{version_number},{datetime.now()},{result},{chosen_word},\""
		for guess in guesses:
			row = row+f"{guess};"
		row = row.rstrip(";")+"\"\n"
		file.write(row)
