import itertools
import string
word_list = []
states = set()

def calculate_states(word):
	word = word.upper()
	letters = set(word)
	for letter in letters:
		states.add(word.replace(letter, "_"))
	two_letters = itertools.combinations(letters, 2)
	for combination in two_letters:
		new_word = word
		for letter in combination:
			new_word = new_word.replace(letter, "_")
		states.add(new_word)
	if len(letters) >= 3:
		three_letters = itertools.combinations(letters, 3)
		for combination in three_letters:
			new_word = word
			for letter in combination:
				new_word = new_word.replace(letter, "_")
			states.add(new_word)
	states.add("____")
	states.add(word)


with open("../common.txt", "r") as common:
	for line in common:
		line = line.strip()
		if len(line) == 4:
			word_list.append(line)
for word in word_list:
	calculate_states(word)
print(len(states))