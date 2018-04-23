import random

answer = random.randint(1,10)

while True:
    user_input = input("Guess the number: ")
    if int(user_input) == answer:
        print("Correct!")
        break
    else:
        print("Wrong, try again!")
