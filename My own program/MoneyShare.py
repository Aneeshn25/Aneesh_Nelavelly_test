#-------------Author------------#
#------------Aneesh-------------#
#-----------version-1.0---------#



def define() :
    print ("\n-----------------")
    print ("Enter the details")
    print ("-----------------")
    global total_mem
    global total_amount
    global total_investors
    total_mem = int(input("Number of persons got involved: "))
    total_amount = int(input("Enter the total amount invested: "))
    total_investors = int(input("Number of persons invested in giving: "))

def sum_avg():
    global avg_amt
    avg_amt = total_amount/total_mem
    return avg_amt

def tot_inv() :
    for i in range(total_investors) :
        print (i+1,")")
        investor_name.append(input("investor name: "))
        invested_amt.append(int(input("invested amount: ")))
    print ("\ninvestor name and amount: ")
    for i in range(total_investors) :
        print (i+1,") ",investor_name[i],", ",invested_amt[i],".")
        
def amt_dist() :
    global j
    j = 0
    total_amt = total_amount
    total_investors_amt = 0
    for i in range(total_investors) :
        total_investors_amt = total_investors_amt + invested_amt[i]
    
    if total_investors_amt == total_amount :
        for i in range(total_investors) :
            # print ("total_amt",total_amt,"invested_amt",invested_amt[i],"avg_amt",avg_amt)
            return_amt.append(invested_amt[i] - avg_amt)
            avg_return_amount.append(return_amt[i]/(total_mem - total_investors))
            total_amt = total_amt - invested_amt[i]
            j = 1
            
    else :
        print ("\nEntered investors amount is not equel with the total invested amount")
        print ("\n----- Try again Thank you -----")
    
def display() :
    print ("\n-------------------------------")
    print ("Amount distribution information")
    print ("-------------------------------")
    print ("")
    print ("Non Investor should return amount:",avg_amt)
    for i in range(total_investors) :
        if return_amt[i] > 0 :
            print ("Investor",investor_name[i],"should get amount of",round(return_amt[i],2),"from other than investors with equal amount of",round(avg_return_amount[i],2))
        elif return_amt[i] == 0 :
            print ("Investor",investor_name[i],"nothing to give or take")
        elif return_amt[i] < 0 :
            print ("Investor",investor_name[i],"should give",round(return_amt[i],2)* -1,"to the investors with equal amount of",round(avg_return_amount[i],2)* -1)
    print ("\n---------- Thank you ----------")

        
def main() :
    while True :
        define()
        tot_inv()
        sum_avg()
        amt_dist()
        if j == 1 :
            display()
        result = input("\nWant to try again(y/n): ")
        k = total_investors - 1
        if result == 'y' :
            for i in range(total_investors) :
                investor_name.pop(k)
                invested_amt.pop(k)
                return_amt.pop(k)
                avg_return_amount.pop(k)
                k = k - 1
            continue
        else :
            break

if __name__ == "__main__":
    # execute only if run as a script
    investor_name = []
    invested_amt = []
    return_amt = []
    avg_return_amount = []
    main()