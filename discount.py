Amount=float(input("Enter Amount used to Purchase: "))
if Amount > 100:
    discount= 0.05*Amount
    print(f"The discount is {discount} only")
else:
    print("No Discount")
