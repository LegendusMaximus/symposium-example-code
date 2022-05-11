input()
# Importing random
import random
# The word list it picks from, add your own words
choice_of_word = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "hello", "december", "george", "today", "adding", "stop", "there"]
word = random.choice(choice_of_word)

guessed = []
# The loop that runs the game, this probably shouldn't be infinite but I was still learning!

while True:
	out = ""
	for letter in word:
		if letter in guessed:
			out = out + letter
		else:
			out = out + "_ "
	print("Guess a letter in the word", out)
	print("It is", int(len(out)/2), "letters long")
	
	guess = input()
	if guess in guessed:
		print("You allready guessed", guess)

	elif guess in word:
		print("YES your guess is a letter in the word.")
		guessed.append(guess)
	else:
		print("NO BOO your letter is  not in the word.")
	input()