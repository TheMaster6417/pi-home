	# Pi Calculator
	# Python 2.7.3
	# After running, type "pi(n)" where n is the number of decimals for pi.  For
	#  example, if you would like to calculate 100 decimals for pi, type "pi(100)".
	
	# import python libraries
	from decimal import Decimal, getcontext
	from time import time, strftime
	import datetime
	
	# arccot function using power formula arccot = 1/x - 1/(3x^3) + 1/(5x^5) ...
	def arccot(x, digits):
	# set precision and starting values
	getcontext().prec = digits
	total = 0
	n = 1
	# loop while new term is large enough to actually change the total
	while Decimal((2 * n - 1) * x ** (2 * n - 1)) < Decimal(10 ** digits):
	# find value of new term
	term = ((-1)**(n - 1)) * 1 / Decimal((2 * n - 1) * x ** (2 * n - 1))
	# add the new term to the total
	total += term
	# next n
	n += 1
	# return the sum
	return total
	
	# pi function
	def pi(decimals):
	# start timer
	timestart = time()
	
	# find pi using Machin's Formula pi = 4 * (4 * arccot(5) - arccot(239))
	#  and the power formula for arccot (see arccot function above)
	print "pi = " + str(Decimal(4 * (4 * arccot(5, decimals + 3) - arccot(239,
	decimals + 3))).quantize(Decimal(10) ** (-decimals)))
	
	# display elapsed time
	timeelapsedint = round(time() - timestart, 2)
	timeelapsedstr = str(datetime.timedelta(seconds = round(
	timeelapsedint, 0)))
	print "runtime: " + timeelapsedstr + " or " + str(
	timeelapsedint) + " seconds
