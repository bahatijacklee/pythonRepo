salary=int(input("Enter your salary: "))
years=int(input("Enter number service years: "))
if years<6:
    bonus=salary*0.05
    NetSalary=salary+bonus

elif years>=6 and years<=10:
    bonus = salary * 0.08
    NetSalary = salary + bonus

elif years>10:
    bonus = salary * 0.1
    NetSalary = salary + bonus

print(f"Your bonus{bonus}")
print(f"Your Net Salary is: {NetSalary}")






