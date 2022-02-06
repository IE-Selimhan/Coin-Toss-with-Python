import time
import random

def coinToss():

	answer = input("are you feeling lucky ?(y/n)\n")
	if answer == 'n':
		print("see you later..")
		return
	if answer == 'y':
		print("we'll see about that :)" )
		time.sleep(1)
		bet = input("Heads or Tails ?(h/t)\n" )
		outcomes = ['h', 't']
		value = random.choice(outcomes)
		if bet in outcomes:
			if bet == value:
				print('great')
			elif bet != value: 
				print('Ooops! Better luck next time.')
		else:
			print("what!?")
			return		

coinToss()

