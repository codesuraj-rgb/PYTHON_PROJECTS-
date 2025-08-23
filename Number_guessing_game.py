# PROJECT 2 - THE PERFECT GUESS

# We are going to write a program that generates a random number and asks the user to
# guess it.
# If the player's guess is higher than the actual number, the program displays "Lower
# number please". Similarly, if the user's guess is too Iow, the program prints "higher
# number please" When the user guesses the correct number, the displays the
# number of guesses the player used to arrive at the number.
# Hint: Use the random module.


import random

r = random.randint(1,100)
guesses = 0

print("🎮 WELCOME TO THE GUESS GAME 🎮")
print("YOU have picked a number between 1 and 100. Try to guess it!\n")

while True :
    g = int(input("👉 Enter your guess: "))
    guesses += 1

    if(g<r):
        print("Higher number please")

    elif(g>r):
        print("lower number please")

    else:
        print(f"✅ YOU GUESSED IT! The number was {r}. Attempts used: {guesses}")
        break

     
    if(guesses==5):
        print(f"you're out off guess .And random number is {r}")
     
        break   
 
    

