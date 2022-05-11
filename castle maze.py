# Press enter at the beginning, this improves accessibility
input()
# Next, import the random module so we can select random numbers
import random
 # Set the treasure variable to a default value of 0
treasure = 0

# Output an introduction message
print("You enter a dark old castle, you are in search of 5 treasures because you need them to get out. Instructions: to go left press l to go straight press s and to go right press r.")
# Create a loop which runs until you get 5 treasures
while treasure < 5:
	# Create our random number
	ran = random.randint(0,4)
	# Ask which direction you would like to go
	user_reply = input("You can go right, left or straight")  
	# Choose what to do based on the direction. This is a very simple example, feel free to change it.
	if user_reply == "l":
		# Tell the user they found treasure and update the treasure variable
		print("You find ", ran,"  treasures!")
		treasure += ran
	elif user_reply == "s":
		# Do the same if they choose straight
		print("You find a bag containing ", ran ," treasures!")
		treasure += ran
	elif user_reply == "r":
		# If they go right, output a message and reset the treasure variable to 0
		print("You go right and find a monster. Your treasures all get stolen and your are let through a trap door back to the beginning")
		treasure = 0

	else:
		# Make users who entered something wrong try again
		print("Sorry, please press l s or r")
# Once the loop ends, output messages telling the user they made it out
print("You have", treasure, "treasures")
print("Your out! you walk out the door into the dark night. You arrive back home!")
# One more input at the end, for accessibility as well
input()


