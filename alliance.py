''' These are the marks for students in Alliance form 4'''
# We declare the number of students
count = input("How many students do you want to compute for: ")

# We loop thru the count n times
# We loop thru count using the variable i(each)
for i in range(0,int(count)):
    name = input("Enter the name of student "+ str(i) +": ")
    admsn = input("Enter the admission number: ")
    maths = input("Enter marks for maths: ")
    english = input("Enter marks for English: ")
    science = input("Enter marks for science: ")
    total = int(maths)+int(english)+int(science)
    mean = int(total)/3
    print("-------------------------------")
   # for t in range(0,i):
    print("|Name\t Admsn\t Maths\t English\t Science\t Total\t Mean|")
    print("------------------------------------")
    print(name+ "\t"+ admsn + "\t" + str(maths) + "\t" + str(english) + "\t" + str(science) + "\t" + str(total) + "\t" + str(mean))
