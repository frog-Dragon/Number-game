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

def guess(numbers:list):
    global guess_corect
    numbers = numbers
    randnum = random.randint(0, len(numbers)-1)
    number = numbers[randnum][0]
    numbers[randnum].pop(0)
    numbers[randnum].append(number)
    if int(input("guess a number: ")) == int(number):
        print("you got it")
        guess_corect = True
    else:
        print("the number was "+str(number))
    return numbers

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
    # variables to change
    rows = 4
    collums = 16

    guess_corect = False
    set_numbers(randomize_numbers(collums, rows))
    set_numbers(get_numbers(), "visible.txt")
    set_numbers(scramble_numbers(get_numbers()))
    while not guess_corect:
        set_numbers(guess(get_numbers()))

main()