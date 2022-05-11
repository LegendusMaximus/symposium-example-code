#Importing modules
import Hangman_engine as engine
import Hangman_save as save
import Hangman_config as config
from datetime import datetime, timedelta

#Setting variables
algorithm_name = "frequency_calculator"
version_number = 0.1
frequency_list = {}
part_word = ""
result = ""
words = []
guesses = []
stop_time = config.run_time

#Loading file
with open ("common.txt", "r") as file:
    for line in file:
        line = line.strip()
        line = line.upper()
        words.append(line)


#Defining functions
def play():
    guesses = []
    part_word = engine.start_game()
    part_word = part_word.upper()
    frequency = calculate(part_word)
    while "_" in part_word:
        old_part_word = part_word
        guess = list(frequency)[0]
        print("Built list")
        guesses.append(guess)
        #print(guess)
        del frequency[guess]
        result, part_word = engine.process_guess(guess)
        #print(f"{result}, {part_word}")
        if old_part_word != part_word:
            print(f"Part word: {part_word}")
            frequency = calculate(part_word)
    save.save_game(algorithm_name, version_number, engine.guesses, result.name, engine.chosen_word)



def calculate(part_word):
    wordlist = []
    #print(len(wordlist))
    for word in words:
        if len(word) == len(part_word):
            wordlist.append(word)
    #print(len(wordlist))
    letters = {}
    for index, item in enumerate(part_word):
        if item != "_":
            for word in wordlist:
                #print(f"{part_word}, {word}, {index}")
                if word[index] != item:
                    wordlist.remove(word)
        for word in wordlist:
            line_letters = set(word)
            for letter in line_letters:
                if letter in letters.keys():
                    letters[letter] = letters[letter]+1
                else:   
                    letters[letter] = 1
    sorted_letters = {k: v for k, v in sorted(letters.items(), key=lambda item: item[1], reverse=True)}
    #print(sorted_letters)
    return sorted_letters

#Running program
while datetime.now() < stop_time:
    play()
