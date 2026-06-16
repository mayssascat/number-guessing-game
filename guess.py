import random
print("welcome to my guessing game")
while True:  # making sure the numbers are integers
    try:
        deb = int(input("Enter deb (must be an integer): "))
        fin = int(input("Enter fin (must be an integer): "))
        break
    except ValueError:
        print("Invalid input. Please enter integers only.")

if fin - deb <= 7:  # making sure the range is larger than there are chances
    print("GOTCHA!you should try a bigger range dawg , periodt")
    deb = int(input("select the start of the range "))
    fin = int(input("select the finale of the range"))

print("You have 7 chances to guess the number right! GOOD LUCK")

num = random.randint(deb, fin)
print("Now we start guessing")
guess = int(input("guess is="))
guesses = 1
ch = 7
while guesses < ch:  # the game is valid for 7 chances
    if guess == num:
        print("guess is correct ,total guesses=" + str(guesses))
        break
    else:
        guesses += 1
    if guess < num:
        print("Too low")
    elif guess > num:
        print("Too high")
    elif guesses == 7:
        print("Sorry , you lost ")
        break

    else:
        print("guess is correct ,total guesses=" + str(guesses))
        break
    guess = int(input("guess is="))


print("Thank you for playing my game ! See you soon XOXO")
