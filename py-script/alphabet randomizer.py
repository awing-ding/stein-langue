import random

PATH = "../alphabet.txt"

def randomizer(path: str)-> None:
    with open(PATH, "r") as file:
        text = file.read()
        text = text.split("\n")
        random.shuffle(text)
        text = "\n".join(text)
    with open(PATH, "w") as file:
        file.write(text)

randomizer(PATH)