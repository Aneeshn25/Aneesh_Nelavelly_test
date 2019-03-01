
def define() :
	global input1
	global input2

	#loop until the user enters valid data
	while True:
		input1 = input(" Enter a value one: ")
		#try for throw and exeption when user enters a invalid data
		try:
			input3 = float(input1)
		except :
			print("Please only numbers are allowed!")
			continue

		input2 = input(" Enter a value two: ")
		try:
			input4 = float(input2)
		except :
			print("Please only numbers are allowed!")
			continue
		
		#comparing both values
		if input3 > input4 :
			print(input3," is grater than ",input4)
		elif input3 < input4 :
			print(input3, " is less than",input4)
		else :
			print("both are equal")
		break

def main() :
	while True:
		define()
		#if user want to try it again
		result = input("\nWant to try again(y/n): ")
		if result == 'y' :
			continue
		else :
			break

if __name__ == "__main__":
	# execute only if run as a script

	main()
