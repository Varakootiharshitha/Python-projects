import random
secret=random.randint(1,20)
attempts =0
print("Guess the number between 1 to 20!")
while True:
    guess=int(input("your guess: "))
    attempts +=1
    if guess<secret:
        print("Too low, try again.")
    elif guess>secret:
        print("Too high,try again.")
    else:
        print(f"correct! you got it in{attempts} attempts.")
        break