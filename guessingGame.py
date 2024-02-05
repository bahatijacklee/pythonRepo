#number guessing game
WinningNumber=4
guess=int(input("Guess a winning number: "))
if guess == 4:
    print("You Win!!!")
else:
   if guess>4:
       print("Your guess is too high")
   elif guess < 4:
       print("You guess is too low")


