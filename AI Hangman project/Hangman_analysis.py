import os
import time
filename = "games.csv"
savefile = "scores.txt"
def percentage_wins():
	tally = {}
	with open(filename, "r") as file:
		file.readline()
		for line in file:
			line = file.readline()
			splitline = line.split(",")
			if len(splitline) < 4:
				break
			game_name = splitline[0]+"_"+splitline[1]
			if game_name not in tally:
				tally[game_name] = {"guesses":0}
			result = splitline[3]
			if result not in tally[game_name]:
				tally[game_name][result] = 0
			tally[game_name][result] = tally[game_name][result]+1
			if result == "SUCCESS":
				guessnumber = (len(splitline[5])+1)/2
				tally[game_name]["guesses"] += guessnumber
#	print(tally)
	for key in tally.keys():
		success_count = float(tally[key]["SUCCESS"])
		failure_count = float(tally[key]["GAME_OVER"])
		total = success_count+failure_count
		fraction = success_count/total
		score = f"{key}: {fraction*100:.2f}%"
		print(score)
		guess_count = float(tally[key]["guesses"])
		average = guess_count/success_count
		file = open(savefile, "a")
		file.write(f"{score} {average}\n")
		file.close()
percentage_wins()