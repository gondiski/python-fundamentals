'''Create student details'''

print("Enter the student names:\n")
# ask for user input
name = input()
print("Enter the student class:\n")
stream = input()
print("Enter the marks maths:\n")
maths = input()
print("Enter the marks english:\n")
english = input()
print("Enter the marks science:\n")
science = input()
print("---------------------\n")
total = int(maths) + int(science) + int(english)
mean = int(total)/3
print("|Student\t English\t Maths\t Science\t Total\t Mean\t ")
print("|" + name + "\t" + str(english) + "\t" + str(maths) + "\t" + str(science) + "\t" + str(total) + "\t" + str(mean) + "|")
