def find(oddOrEven, numberRange):
	if oddOrEven == "even":
		n = 0
		for i in range(1, (numberRange + 1)):
			if n % 2 == 0:
				print(n)
			n = (n + 1)
			
	elif oddOrEven == "odd":
		n = 1
		for i in range(1, (numberRange + 1)):
			if n % 2 == 1:
				print(n)
			n = (n + 1)
