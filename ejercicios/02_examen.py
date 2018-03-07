


""" Corrige el siguiente script, recuerda hacer commits cada 5 minutos """

import random

for i in range (0, 11):
	a = random.randint(1,12)
	b = random.randint(1,12)
	question = "What is {} X {}?".format(a,b)
	answer = int(input(question))
	if answer == a * b:		
		print("Well done!")
	else:
		print("No.")