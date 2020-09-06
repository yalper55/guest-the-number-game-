import random


guess_number = random.randint(0, 10)

print(guess_number)
number = int(input())


if number > guess_number:
    print("too high")
elif number < guess_number:
    print("too low")
else:
    print("you win")
