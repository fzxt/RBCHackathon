from random import randint
import random

folder = "Customers/"
f = open(folder + "c1.txt","w+")

# problem, our solution, why it is special
# say that this is secure. Secirity key
# building relationships with Customers


numDays = [31,28,31,30,31,30,31,31,30,31,30,31]
year = 2016


# date, amount, name, notes
#

# set up the expenses that c1 has: how many times / month, total cost, % deviance
c1 = [(0,"Rent", 1000, 0),(4, "Supplies", 1500, 10),(2, "Gas", 500, 5),(0, "Employee", 1040, 0)]
#rent due date
rent_due = 1
# employee pay date
tmp = randint(1,14)

payEmp = (tmp, tmp+14)

print ("Pay Emps on: " + str(payEmp))

#number of employees
numEmployee = randint(1,5)


for month in range(0,len(numDays)):
    #keep a counter for each month
    count = []
    # keep a running total of how much was spent
    total = []
    for data in c1:
        count.append(data[0])
        total.append(data[2])
    # write the transactions
    # print (str(count) + "\n" + str(total))
    for day in range (1,int(numDays[month])+1):
        if (day == rent_due):
            print ("Paying rent")
            for expense in c1:
                if (expense[1] == "Rent"):
                    f.write(str(year) +"-"+str(month+1).zfill(2)+"-"+str(day).zfill(2)+",")
                    f.write("-"+str(expense[2]) + "," + "Landlord,Rent\n")

        if ((day == payEmp[0]) | (day == payEmp[1])):
            print ("Paying employees")
            for expense in c1:
                for i in range(numEmployee):
                    if (expense[1] == "Employee"):
                        print ("Paying employee " + str(i))
                        f.write(str(year) +"-"+str(month+1).zfill(2)+"-"+str(day).zfill(2)+",")
                        f.write("-"+str(expense[2]) + "," + "Employee,Paycheck\n")
        for i in range(len(c1)):
            expense = c1[i]
            if (expense[0] != 0 & randint(0,100) < 10):
                current_cost = float(expense[2])*float(randint(1,50)/100)
                total = float(current_cost) + (float(current_cost) * ((randint(-expense[3], expense[3]))/100))
                f.write(str(year) +"-"+str(month+1).zfill(2)+"-"+str(day).zfill(2)+",")
                f.write("-"+str(total) + "," + "Payable," + expense[1] + " \n")
        cust = randint(1,50)
        for i in range(1,cust):
            spent = random.uniform(5, 200)
            f.write(str(year) +"-"+str(month+1).zfill(2)+"-"+str(day).zfill(2)+",")
            f.write(str(spent) + "," + "Customer," + "Purchase" + " \n")


f.close()
