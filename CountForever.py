input()
import time
import os
# This is just for fun
# Warning! Don't just leave this running all day, it could crash
# JAWS/NVDA won't read it very well
count = 0
while True:
	print(count)
	time.sleep(1)
	os.system("cls")
	count += 1
	
input()