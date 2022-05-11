input()
score = {}
	
import requests
import random
import smtplib
from shutil import copyfile
import os
import json
# This code will not run in this state due to it using an API which is private and has been removed from the code. Please take out all references to the API first! If you have already done this, remove the comment

login = False
# Deleted actual URL for privacy, make your own rest API or remove it
url = "https://xxxxxxxxxxx.azurewebsites.net/api/"
def get_scores():
    response = requests.get(url+"scores/")
    if response.ok:
        return json.loads(response.text)

def loadwords():
	file = open("common.txt")
	dictionarywords = []
	for line in file:
		word = line.strip()
		if len(word) >= 4:
			dictionarywords.append(word)
	return dictionarywords


def getusers():
	response = requests.get(f'{url}users/')
	if response.ok:
		return json.loads(response.text)
	
def hash(pass1):
	passhash = 0
	for character in pass1:
		passhash += ord(character)
	return passhash

def createuser(username1):
	global email
	user = {"Username":username1}
	user["Email"] = input("Please enter an email address\n")
	password = input("please create a password\n")
	user["PasswordHash"] = hash(password)
	#print(passhash)
	#response = requests.post(url+"users/",json = "{\"Username\":\""+username1+"\", \"Email\":\""+email+"\", \"PasswordHash\":"+str(passhash)+"}")
	response = requests.post(f'{url}users/',json=user)
	print(response)
	email = user["Email"]
	login = True

	

users = getusers()

while login == False:	
	username = input("Type a username here to login or create an account\n")
	match = None
	for user in users:
		if username == user["Username"]:
			match = user
			break
	if match:
		password = input("Enter your password \n")
		passhash = hash(password)
		if passhash == match["PasswordHash"]:
			print("You are logged in")
			email = match["Email"]
			login = True
		#else:	
			#print("please try again")
	else:
		createuser(username)
		break


name = username
all_scores = get_scores()
matchinguserscore = None
for score in all_scores:
	if score["Username"] == username:
		matchinguserscore = score 
if matchinguserscore:
	print("Your scores are", matchinguserscore["Scores"]) 
	userscores = matchinguserscore["Scores"]
else:
	userscores = ""




	
		
		
		
		
	

highest = -1 
print("Welcome to Theo's hangman game!")

tries = 0
#choice_of_word = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "hello", "december", "george", "today", "adding", "stop", "there", "wifi", "january", "febuary", "march", "april", "may", "june", "july", "august", "september", "october", "november", "house", "room", "eating", "food", "water", "cups", "networks", "table", "drawer"]
choice_of_word = loadwords()
word = random.choice(choice_of_word)

guessed = []
while True:
	out = ""
	for letter in word:
		if letter in guessed:
			out = out + letter + " "
		else:
			out = out + "_ "
	outnospaces = out.replace(" ", "")
	if outnospaces == word:
		
		print("Well Done ", name, "! You guessed the word, it was", 		word, " in", tries, "wrong guesses")
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
		


	else:
		tries += 1

		print("NO BOO ", name, " your letter is  not in the word. You have had ", tries, "out of 20 possible wrong guesses before you are hung.")
		guessed.append(guess)
	input("Press enter to  guess another letter")
	os.system("cls")
	if tries == 20:
		print("Boo", name, "You lost, you have ran out of tries so you have been hung. The word was", word, )
		input()
		break
userscores = userscores+";"+str(tries)
if matchinguserscore:
	scoreid = matchinguserscore["Id"]
	del matchinguserscore["Id"]
	del matchinguserscore["Updated"]
	response = requests.put(f"{url}scores/{scoreid}", json=matchinguserscore)
	print(response)
else:
	userscores = ";"+str(tries)
	score["Email"] = email
	score["Username"] = username
	score["Scores"] = userscores
	response = requests.post(f'{url}scores/', json=score) 
