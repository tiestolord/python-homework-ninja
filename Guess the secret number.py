# Guess the secret number

secret = 7

name = input("Hey there you, whats your name?")
guess = int(input("Good,can you guess the lucky number " + name +"?"))

if guess == 7:
    print("Wooow, you did it!!!")

else:
    print("Sorry "+ name +" you need to guess better")

