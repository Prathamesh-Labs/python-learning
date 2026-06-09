import random
secret_number = random.randint(1,100)
print("Welcome to The most uncommon made by Prathamesh Labs game Which is Number Guessing Game!")
name = input("Enter your name: ")
attempts = 0
while True:
    guess = int(input("Enter your guess: "))
    difference = abs(secret_number- guess)
    attempts += 1
    if difference <=5:
        print("Very Close!")
    elif difference <= 15:
        print("Close!")
    else:
        print("Far Away!")
    if guess == secret_number:
        print(name ," guessed it!")
        print("Attempts:",attempts)
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too High!")