input()
# Imports
import random
import os
# Welcome message
print("Welcome to Theo's hangman game!")
# Variables, some of which user enters
name = input("Please enter your name to continue")
tries = 0
choice_of_word = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "hello", "december", "george", "today", "adding", "stop", "there", "wifi", "january", "febuary", "march", "april", "may", "june", "july", "augaust", "september", "october", "november", "house", "room", "eating", "food", "water", "cups", "networks", "table", "drawer"]
word = random.choice(choice_of_word)

guessed = []
# The loop that runs the game, this probably shouldn't be infinite but I was still learning!
while True:
	out = ""
	for letter in word:
		if letter in guessed:
			out = out + letter + " "
		else:
			out = out + "_ "
	outnospaces = out.replace(" ", "")
	if outnospaces == word:
		
		print("Well Done ", name, "! You guessed the word, it was", word, " in", tries, "guesses")
		input()
		break
	print(name, ", Guess a letter in the word", out)
	print("It is", int(len(out)/2), "letters long")
	
	guess = input()
	if guess in guessed:
		print(name, " You already guessed", guess)

	elif guess in word:
		print("YES ", name, " your guess is a letter in the word.")
		guessed.append(guess)
		tries += 1


	else:
		print("NO BOO ", name, " your letter is  not in the word.")
		tries += 1
		guessed.append(guess)
	input("Press enter to  guess another letter")
	os.system("cls")
	if tries == 20:
		print("Boo", name, "You lost, you have ran out of tries so you have been hung. The word was", word, )
		input()
		break