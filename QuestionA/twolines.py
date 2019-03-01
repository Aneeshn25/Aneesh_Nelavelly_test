#-------------Author------------#
#------------Aneesh-------------#

def define() :
	while True:
		print ("\n---------------------------------------------------------")
		y = 1
		for x in range(2) :
			print("Enter coordinate for line #",x+1)
			#try to throw an exception when user enters a invalid data
			try :
				point1.append(float(input("Enter x{0} in coordinate #{1}:".format(y,x+1))))
			except :
				print("Only takes numerics! \nplease try again")
				exit()
			try :
				point2.append(float(input("Enter x{0} in coordinate #{1}:".format(y+1,x+1))))
			except :
				print("Only takes numerics! \nplease try again")
				exit()
			y = y + 2
		#swaping if first coordinate are not in an assending order
		if point1[0]>point2[0]: 
			i = point1[0]
			point1[0] = point2[0]
			point2[0] = i
		#print("point1[0]",point1[0],"point2[0]",point2[0],"point1[1]",point1[1],"point2[1]",point2[1])
		#logic goes true if one coordinate falls between the other coordinate
		if ((point1[0] <= point1[1]) & (point1[1] <= point2[0]) | (point1[0] <= point2[1]) & (point2[1] <= point2[0]) ) :
			print("Both the lines overlap on x-axis")
		else :
			print("They don't overlap")
		break


def main() :
	while True:
		define()
		result = input("\nWant to try again(y/n): ")
		a = 1
		if result == 'y' :
			for i in range(2):
				#popping out the data from the array to try it again
				point1.pop(a)
				point2.pop(a)
				a = a - 1
			continue
		else :
			break

if __name__ == "__main__":
	# execute only if run as a script
	point1 = []
	point2 = []

	main()