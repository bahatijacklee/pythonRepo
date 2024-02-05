age= int(input("Enter your age: "))
country= input("Enter your country: ")
if age>=18 and  country in ["kenya","tanzania","uganda"]:
    print("eligible to vote")
else:
    print("not eligible to vote")

print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))
print(2%6)
print(2 * 3 ** 3 * 4)
print(-18 // 4)