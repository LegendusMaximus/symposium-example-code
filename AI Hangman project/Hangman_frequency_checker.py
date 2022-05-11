words = open("common.txt")
letters = {}

for line in words:
	line = line.strip()
	if len(line) == 4:
		line = line.upper()
		line_letters = set(line)
		for letter in line_letters:
			if letter in letters.keys():
				letters[letter] = letters[letter]+1
			else:
				letters[letter] = 1
			#print(f"{letter}: {letters[letter]}")

sorted_letters = {k: v for k, v in sorted(letters.items(), key=lambda item: item[1], reverse=True)}

print(sorted_letters)