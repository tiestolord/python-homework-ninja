#The mood checker

user_name = input("Enter your name: ")

if user_name:
    input("After this part enter the mood how you feel " + user_name+". Press Enter to continue.")
    user_mood = input("Enter your mood: ")



if user_mood == "Happy":
    print("It is great to see you happy!")

elif user_mood == "Sad":
    print("Dont be, life is beautiful!")

elif user_mood == "Relaxed":
    print("Lets keep chilling then.")

elif user_mood == "Nervous":
    print("Take a deep breath 3 times.")

else:
    print("I don't recognize this mood.")


