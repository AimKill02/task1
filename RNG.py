import random
min = 1
max = 100
Number = random.randint(min,max)
def final():
    while True:
        try:
            guess = int(input(f"Choose between {min} to {max}: "))
            if min <= guess <= max:
                return guess
            else:
                print("Number invalid")
        except ValueError:
            print("Input invalid")
def checksum(guess, Number):
    if guess == Number:
        return "Correct"
    elif guess < Number:
        return "higher"
    else:
        return "lower"
def attempts():
    X = 0
    while X >=0:
        X += 1
        guess = final()
        result = checksum(guess, Number)
        if result == "Correct":
            print(f"You got the answer, the answer is {Number}")
            break
        else:
            print(f"Your answer should be {result} than {guess}")
            print(f"Amount you tried: {X}")
attempts()