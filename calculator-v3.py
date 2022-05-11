input()
file = open("calculatorhistory.txt", "w")
clear = "f"
while True:

		
	operation = input("Press d to divide, a to add, s to subtract and m to multiply press c to clear and press e to exit")
	if operation == "e":
		break
	number1 = int(input("Enter number"))
	number2 = int(input("Enter a number to do the operation you selected  to the first number"))
	if operation == "a":
		result = number1+number2
		print(result)
	if operation == "m":
		result = number1*number2
		print(result)
	if operation == "d":
		result = number1/number2
		print(result)
	if operation == "s":
		result = number1-number2
		print(result)
	if operation == "c":
		result = 0
	filewrite1 = str(number1)
	filewrite2 = str(number2)
filewriteoperation = str(operation)
filesave = str(number1+filewriteoperation+number2)
file.write(filesave)





while clear == "f":
	
		if result != "0":
			recalculate = input("Press e to close this program or press d to divide your answer to the last operation, m to multiply, a to add and s to subtract or press c to clear")
			if recalculate == "c":
				result = 0
			if recalculate != "e":
				number3 = int(input("Enter a number"))
				if recalculate == "s":
					result2 = result-number3
					print(result2)
				elif recalculate == "d":
					result2 = result/number3
					print(result2)
				elif recalculate == "a":
					result2 = result+number3
					print(result2)
				elif recalculate == "c":
					clear == "t"
				else:
					break
				print("To calculate another sum enter a number below, otherwise, press c and then press enter twice to close this program")
		operation = input("Press d to divide, a to add, s to 	subtract and m to multiply press c to clear and press e to exit")
		if operation == "e":
			break
		number1 = int(input("Enter number"))
		number2 = int(input("Enter a number to do the operation you selected  to the first number"))
		if operation == "a":
			result = number1+number2
			print(result)
		if operation == "m":
			result = number1*number2
			print(result)
		if operation == "d":
			result = number1/number2
			print(result)
		if operation == "s":
			result = number1-number2
			print(result)
		if operation == "c":
			result = 0
			filewrite1 = str(number1)
			filewrite2 = str(number2)
filesave = number1+operation+number2
file.write(filesave)

if operation != "e":
	input()
	
		