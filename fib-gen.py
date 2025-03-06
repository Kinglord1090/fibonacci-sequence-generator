# Variables
first = 0
second = 1
sequence = []
method = input("Type 1 to enter the amount of numbers to be generated.\n"
               "----------OR----------\n"
               "Type 2 to enter the approximate biggest number in the sequence.\n")
output_form = input("Type 1 to get a list of all the numbers.\n"
                    "----------OR----------\n"
                    "Type 2 to get all the numbers displayed vertically.\n")


# Solver
def printer(first, amount_of_numbers=0):
	if output_form == "1" or output_form.lower() == "one":
		sequence.append(first)
		if len(sequence) == amount_of_numbers:
			print(sequence)
	elif output_form == "2" or output_form.lower() == "two":
		print(first)


def method1(first, second):
	for number in range(amount_of_numbers):
		printer(first, amount_of_numbers)
		new = first + second
		first = second
		second = new


def method2(first, second):
	while first <= maximum:
		printer(first)
		new = first + second
		first = second
		second = new
	if output_form == "1" or output_form.lower() == "one":
		print(sequence)


if method == "1" or method.lower() == "one":
	amount_of_numbers = int(input("Enter the amount of numbers to be generated: "))
	method1(first, second)
elif method == "2" or method.lower() == "two":
	maximum = int(input("Enter the approximate biggest number in the sequence: "))
	method2(first, second)
