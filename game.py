import random
def set_numbers(numbers:list, file:str = "numbers.txt"):
    txt = ""
    for i in numbers:
        for j in i:
            txt += str(j)+","
        txt = txt.removesuffix(",")
        txt += "\n"
    txt = txt.removesuffix("\n")
    with open(file, "w") as f:
        f.write(txt)

def get_numbers(file:str = "numbers.txt"):
    with open(file, "r") as f:
        ls = f.read().split("\n")
        for i in ls:
            ls[ls.index(i)] = i.split(",")
        return ls

def guess_number(numbers:list, guess:int, win_text:str= "you got it", loose_text:str= "the number was \#"):
    guess_corect = False
    numbers = numbers
    randnum = random.randint(0, len(numbers)-1)
    number = numbers[randnum][0]
    numbers[randnum].pop(0)
    numbers[randnum].append(number)
    if guess == int(number):
        print(win_text.replace("\#", number))
        guess_corect = True
    else:
        print(loose_text.replace("\#", number))
    set_numbers(numbers)
    return guess_corect

def randomize_numbers(colloms:int, rows:int):
    numbers = []
    for i in range(colloms):
        numbers.append([])
        for _ in range(rows):
            numbers[i].append(random.randint(1, 100))
    return numbers

def scramble_numbers(numbers):
    for i in numbers:
        for _ in range(random.randint(0, 99)):
            number = numbers[numbers.index(i)][0]
            numbers[numbers.index(i)].pop(0)
            numbers[numbers.index(i)].append(number)
    return numbers

def main():
    import os
    # variables to change
    rows = 16
    collums = 4

    guess_corect = False
    set_numbers(randomize_numbers(collums, rows))
    set_numbers(get_numbers(), "visible.txt")
    set_numbers(scramble_numbers(get_numbers()))
    tries = 0
    last_guess = None
    while not guess_corect:
        guess = int(input("Guess a number: "))
        if guess != last_guess:
            tries += 1
            guess_corect = guess_number(get_numbers(), guess, "You got it in "+str(tries)+" tries.", "You didn't get it, the number was \#.")
            last_guess = guess
        else:
            print("Your number can not be the same as your last number")
    os.remove("visible.txt")
    os.remove("numbers.txt")

main()