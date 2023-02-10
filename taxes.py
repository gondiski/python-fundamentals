'''This is how to calculate tax'''
name = input("Enter the name of the employee: ")
salary = input("Enter the salary of the employee: ")
nhif = 1000
nssf = 200
while int(salary) > int(24000):
    if int(salary) <= int(24000):
        tax = float(salary) + float((int(salary)-int(24000))*(10/100))
    elif int(salary) >= int(24000) and int(salary) <= int(32300):
        tax = float(salary) + float((int(salary)-int(32300))*(25/100))
    else:
        tax = float(salary) + float(int(salary)*(30/100))
    net_pay = float(salary) + float(tax) + float(nhif) + float(nssf)
    print("Gross pay: " + str(salary))
    print("Net pay: " + str(net_pay))
    break
print("End")
