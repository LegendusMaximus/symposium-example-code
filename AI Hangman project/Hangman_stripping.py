raw_file = open("common_raw.txt")
new_file = open("common.txt", "w")
for line in raw_file:
	line = raw_file.readline()
	line = line.strip("\n")
	if len(line) < 4:
		continue
	if "-" in line:
		continue
	if "'" in line:
		continue
	print(line)
	new_file.write(line+"\n")
print("Task complete")
input("Press enter to close")