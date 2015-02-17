list_range = range(1, 20, 3)
i = raw_input ("Guess if a number is a part of the range: ")
if int(i) in list_range:
	print "Correct, " + str(list_range)
else:
	print "Try again"