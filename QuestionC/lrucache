from datetime import datetime  
from datetime import timedelta 
from collections import deque

time_stamp = []
cache = deque([])

#takes the data from the user side

def data_input() :
	lenofcache = len(cache)
	#if it already reached the max size
	if lenofcache == MAX :
		cache.pop()
		cache.appendleft(input("Enter the data to cache: "))
		time_stamp.append(datetime.now())
		time_stamp.pop()
		print("reached max now popping out the least used")
		print("list:",cache)
		input_data_again()
	#if it does'nt yet reached the max size
	else :
		cache.appendleft(input("Enter the data to cache: "))
		time_stamp.append(datetime.now())
		print("list:",cache)
		input_data_again()

#function to input the data again
def input_data_again():
	i = (input("want to enter data again?(y/n)"))
	if i == 'y':
		data_input()
	elif i == 'n' :
		main()
	else:
		print("Only takes y or n as input\n try again")
		input_data_again()

#display cache data
def display() :
	print("\nhere is the cache data:")
	print("-------------------------")
	print("cache data  &  time stamp")
	print("-------------------------")

	lenofcache = len(cache)
	a = lenofcache - 1
	for x in range(lenofcache):
		time = datetime.now() - time_stamp[a]
		a = a-1
		if time > timedelta(seconds=30):
			time_stamp.pop()
			cache.pop()
			print("data ",x+1," got expired")

	lenofcache = len(cache)
	for x in range(lenofcache):
		print(x+1,") ",cache[x]," ",time_stamp[x])
	print("-------------------------")


#to give the user to access the data and make the cache follow LRU
#the accessed data in the cache gets shift to top of the list and the rest shit one position down
def access():
	try:
		i = int((input("data that you want to access : ")))
		j = i-1
		if i != 1:
			print("data from cache just been accessed now")
			for x in range(i-1):
				k = cache[j]
				cache[j] = cache [j-1]
				cache[j-1] = k
				k = time_stamp[j]
				time_stamp[j] = time_stamp [j-1]
				time_stamp[j-1] = k
				j = j-1
			time_stamp[j] = datetime.now()
		else :
			time_stamp[0] = datetime.now()
	except:
		print("data expiered or not here")
	display()
	access_again()
		

#function for if user want to access the data again
def access_again() :	
		k = (input("want to access data again?(y/n)"))
		if k == 'y':
			access()
		elif k == 'n' :
			main()
		else:
			print("Only takes y or n as input\n try again")
			access_again()
#function that has other functions to access the data
def access_cache() :
	display()	
	access()
	display()
	access_again()

def main():
	
	while True :
		print("===========================")
		print("Menu: \n 1)Enter data into cache \n 2)access cache \n 3)exit")
		print("===========================")
		result = input("Enter your option: ")
		if result == "1"  :
			data_input()

		elif result == "2" :
			access_cache()

		elif result == "3" :
			exit()	
		else :
			print ("Chosen a wrong option \n please try again")
		continue
	

if __name__ == "__main__":
	# execute only if run as a script

	MAX = 5
	main()
