age= int(input("Enter your age: "))
country= input("Enter your country: ")
if age>=18 and  country in ["kenya","tanzania","uganda"]:
    print("eligible to vote")
else:
    print("not eligible to vote")