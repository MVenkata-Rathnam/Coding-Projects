import random
print "Welcome to the game of hand cricket!!!";
print "\nRules to be followed:-";
print "1. The batsman and bowler must only choose a number between 0 and 10."
print "2. If a number is chosen out of range, the game will be ended."
print "3. The batsman will be out if he/she hit three consecutive zeros.\n"
choice = raw_input("\nChoose odd or even: ");
input1 = raw_input("\nEnter a number ( 0 - 10 ): ");
input2 = random.randrange(0,10,1);
choice1 = None
choice2 = None
total_Score_User = 0;
total_Score_Computer = 0;
UserScore = 0;
countZero = 0;
ComputerScore = 0;
if((int(input1) + int(input2))%2 == 0 and choice == "even"):
	flag = 1
	print "Congratulations! You won the toss!"
elif((int(input1) + int(input2))%2!=0 and choice == "odd"):
	flag = 1
	print "Congratulations! You won the toss!"
else:
	flag = 0
	print "\nBad Luck! Computer won the toss!"
if(flag == 0):
	print "Computer has to choose either to bat or bowl!!!";
	choice1 = random.choice(["Bat","Bowl"]);
	print "\nComputer has opted to " + choice1 + " first."	
if(flag == 1):
	choice2 = raw_input("\nChoose your choice (Bat or Bowl): ")
	print "\nUser has opted to " + choice2 + " first."
if(choice1 == "Bowl" or choice2 == "Bat"):
	print "\nFirst Innings :- \n\tBatting - User\n\tBowling - Computer\n"
	while(countZero < 3):
		UserScore = raw_input("\nEnter a number ( 0 - 10): ");
		ComputerScore = random.randrange(0,10,1);
		print "The computer has bowled " + str(ComputerScore)		
		if(int(UserScore) == 0):
			countZero = countZero + 1
		elif(int(UserScore) == ComputerScore):
			print "Computer has bowled you out!!"
			break
		else:
			if(countZero > 0):
				countZero = countZero - 1
			total_Score_User = total_Score_User + int(UserScore)
	if(countZero >=3):	
		print "\nYou have entered three consecutive zeros!!";	
	print "\nAfter First Innings - Your total score is " + str(total_Score_User);
	print "\nNow its turn for you to bowl!!";
	countZero = 0
	print "Second Innings :- \n\tBatting - Computer\n\tBowling - User"
	while(countZero < 3 and total_Score_Computer <= total_Score_User):
		UserScore = raw_input("\nEnter a number ( 0 - 10): ");
		ComputerScore = random.randrange(0,10,1);
		print "The computer has hit " + str(ComputerScore)		
		if(ComputerScore == 0):
			countZero = countZero + 1
		elif(int(UserScore) == ComputerScore):
			print "You have bowled out computer!!"			
			break
		else:
			if(countZero > 0):
				countZero = countZero - 1;
			total_Score_Computer = total_Score_Computer + ComputerScore
	if(countZero >=3):
		print "\nComputer has entered three consecutive zeros!!";	
	print "\nAfter Second Innings - Computer's total score is " + str(total_Score_Computer);
	if(total_Score_Computer > total_Score_User):
		print "Sorry! Computer won the game!!"
	elif (total_Score_User > total_Score_Computer):
		print "Congratulations! You won the game!!"
	else:
		print "The game ended in a draw!!"
else:
	print "First Innings:- \n\tBatting - Computer\n\tBowling - User" 
	while(countZero < 3):
		UserScore = raw_input("\nEnter a number ( 0 - 10): ");
		ComputerScore = random.randrange(0,10,1);
		print "The Computer has hit " + str(ComputerScore)		
		if(int(UserScore) == 0):
			countZero = countZero + 1
		elif(int(UserScore) == ComputerScore):
			print "You have bowled computer out!!"
			break
		else:
			if(countZero > 0):
				countZero = countZero - 1
			total_Score_User = total_Score_User + int(UserScore)
	if(countZero >=3):	
		print "\nComputer has entered three consecutive zeros!!";	
	print "\nAfter First Innings - Computer's total score is " + str(total_Score_User);
	print "\nNow its turn for you to bat!!";
	countZero = 0
	print "Second Innings:- \n\tBatting - User\n\tBowling - Computer"
	while(countZero < 3 and total_Score_User<=total_Score_Computer):
		UserScore = raw_input("\nEnter a number ( 0 - 10): ");
		ComputerScore = random.randrange(0,10,1);
		print "The computer has bowled " + str(ComputerScore)		
		if(ComputerScore == 0):
			countZero = countZero + 1
		elif(int(UserScore) == ComputerScore):
			print "Computer has bowled you out!!"			
			break
		else:
			if(countZero > 0):
				countZero = countZero - 1;
			total_Score_Computer = total_Score_Computer + ComputerScore
	if(countZero >=3):
		print "\nYou have entered three consecutive zeros!!";	
	print "\nAfter Second Innings - Your total score is " + str(total_Score_Computer);
	if(total_Score_Computer > total_Score_User):
		print "Sorry! Computer won the game!!"
	elif (total_Score_User > total_Score_Computer):
		print "Congratulations! You won the game!!"
	else:
		print "The game ended in a draw!!"
print "\nThanks for playing!!Try it again!!!"

