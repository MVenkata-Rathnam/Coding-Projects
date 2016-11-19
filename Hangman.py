def hangman(count):
	if(count == 1):
		print " o"
		print " "
		print " "
		print " "
	elif(count == 2):
		print " o"
		print "","|"
		print " "
		print " "
	elif(count == 3):
		print " o"
		print "\|"
		print " "
		print " "
	elif(count == 4):
		print " o"
		print "\|/"
		print " "
		print " "
	elif(count == 5):
		print " o"
		print "\|/"
		print " |"
		print " "
	elif(count == 6):
		print " o"
		print "\|/"
		print " |"
		print "/"
	else:
		print " o"
		print "\|/"
		print "","|"
		print "/ \\"
print "Welcome to hangman. You get seven chances to guess the mystery word."
count = 0;
list1 = ['_','_','_','_','_','_','_']
list2 = ['C','R','I','C','K','E','T']
list3 = []
while(count < 7):
	flag = 0
	char = raw_input('Pick a letter --> ')
	char = char.upper()
	if(char.isdigit()):
		print "'" + char +"' is not a valid letter"
		continue
	if(len(char) > 1):
		print "'" + char.upper() + "' has more than one character"
		continue	
	for i in list1:
		if(char == i):
			flag = 1
			print "Sorry, you already guessed '"+ char +"'";
			break; 
	if(flag == 0):
		list3.append(char)
		count = count + 1	
		index1 = 0;		
		for i in list2:
			if i.upper() == char:
				list1[index1] = char
			index1 = index1 + 1
		print "Guessed letters: ",
		for i in list3:
			print i,
	print "\n"
	hangman(count)
	print " "	
	for i in list1:
		print i,
	print '\n '
if '_' in list1:
	print "So sorry. You struck out."
else:
	print "You Successfully found the word."
print "The mysterious word was '",
print ''.join(list2),
print "'."

