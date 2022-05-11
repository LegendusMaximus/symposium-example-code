input()
goki_left = 40
score = 0
import random

colour_taken = "poop"

def red_goki():
	global goki_left, score
	goki_left = goki_left - 1
	random_red  = random.randint(0,100)
	if random_red >= 70 and goki_left >= 20:
		print("Moved")
	elif random_red >= 80 and goki_left <= 20:
		print("Moved")
	else:
		random_red	= random.randint(0,100)
		if random_red >= 70 and goki_left >= 20:
			print("Moved")
		elif random_red >= 80 and goki_left <= 20:
			print("Moved")
		else:
			print("Won")
			score = score + 1
	
def green_goki():
	global goki_left, score
	goki_left = goki_left - 1
	random_green = random.randint(0,100)
	if random_green >= 60 and goki_left >= 20:
                print("Moved.")
	elif random_green >= 70 and goki_left <= 20:
                print("Moved.")
	else:
		print("Won.")
		score = score + 2

def blue_goki():
	global goki_left, score
	goki_left = goki_left - 1
	random_blue = random.randint(0,100)
	if random_blue >= 50 and goki_left >= 20:
		print("Moved")
	elif random_blue >= 60 and goki_left <= 20:
		print("Moved")
	else:
		print("Won")
		score = score + 3
		goki_left = goki_left - 1
		random_green = random.randint(0,100)
		if random_green >= 60 and goki_left >= 20:
			print("Moved.")
		elif random_green >= 70 and goki_left <= 20:
			print("Moved.")
		else:
			print("Won.")
		score = score + 2

def blue_goki():
	global goki_left, score
	goki_left = goki_left -1
	random_blue = random.randint(0,100)
	if random_blue >= 50 and goki_left >= 20:
		print("Moved")
	elif random_blue >= 60 and goki_left <= 20:
		print("Moved")
	else:
		print("Won")
		score = score + 3
while goki_left != 0:
	colour_taken = input("Type red, green or blue. Reds are less likely to make the rat-trap move, green are medium likely to make the rat-trap to move and the blues are more likely for the rat-trap to move.")
	if colour_taken == "red":
		red_goki()
	elif colour_taken == "blue":
		blue_goki()
	else:
		green_goki()
print("You got ", score, "points and you could have got 120 points!")
input()