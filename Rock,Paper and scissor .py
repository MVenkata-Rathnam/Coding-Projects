import random
humanCount = 0;
systemCount = 0;
print "Welcome to Rock, Paper, Scissors!"
pt = raw_input("How many points are required for a win? ")
while(humanCount < int(pt) and systemCount < int(pt)):
	choice1 = raw_input("Choose (R)ock, (P)aper, or (S)cissors?")
	choice2 = random.choice(["r","p","s"]);
	if(choice1 is choice2):
		if(choice1 is "r"):
			print "Human: rock\tComputer: rock\tA draw"
		elif(choice1 is "p"):
			print "Human: paper\tComputer: paper\tA draw"
		else:
			print "Human: scissors\tComputer: scissors\tA draw"
	elif(choice1 is "r" and choice2 is "p"):
		systemCount = systemCount + 1
		print "Human: rock\tComputer: paper\tComputer wins!"
	elif(choice1 is "r" and choice2 is "s"):
		humanCount = humanCount + 1
		print "Human: rock\tComputer: scissors\tHuman wins!"
	elif(choice1 is "s" and choice2 is "p"):
		humanCount = humanCount + 1
		print "Human: scissors\tComputer: paper\tHuman wins!" 
	elif(choice1 is "p" and choice2 is "r"):
		humanCount = humanCount + 1
		print "Human: paper\tComputer: rock\tHuman wins!"
	elif(choice1 is "s" and choice2 is "r"):
		systemCount = systemCount + 1
		print "Human: scissors\tComputer: rock\tComputer wins!"
	elif(choice1 is "p" and choice2 is "s"):
		systemCount = systemCount + 1
		print "Human: paper\tComputer: scissors\tComputer wins!"
	print""
print "Final Score: Human " + str(humanCount) + " Computer " + str(systemCount)	

