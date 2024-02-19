score1=int(input("Enter first score: "))
score2=int(input("Enter second score: "))
score3=int(input("Enter third score: "))
average= (score1+score2+score3)/3

if average <=70 and average <=100:
  print("A")

elif average >=60 and average <=69:
  print("B")

elif average >= 50 and average <= 59:
  print("C")

elif average >= 40 and average <= 49:
  print("D")

elif average >=0 and average <= 39:
  print("Fail")


