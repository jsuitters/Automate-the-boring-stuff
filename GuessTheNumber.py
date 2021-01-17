import random
print("I am thinking of a number between 1 and 20...")
number = random.randint(1, 20)
print(number)

for n in range(1, 7):
    numberGuess = int(input("Take a guess!"))
    if numberGuess > number:
        print("Too high!")
    elif numberGuess < number:
        print("Too low!")
    else:
        break

if numberGuess == number:
    print("Correct.You guessed the number in " + str(n) + " tries" )
else:
    print("You didn't get it. The number was " + str(number))

