import random
from random import seed
from random import randint
fullEmail = 0
password = 0

randomSeedNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ["~", "!", "@", "#", "$", "&", "*"]
words = ['red', 'dog', 'kitten', 'book', 'bowl', 'bulb', 'ink', 'cat', 'bot', 'cup', 'bear', 'word', 'mice', 'mat']

seed(random.choice(randomSeedNumber))

name = input("What is your full name with no spaces in between (no middle name)? ")
numberAtStart = input("What are some numbers you want to add to the start? Leave blank for none. ")

email = numberAtStart + name
fullEmail = email + str(randint(1, 10000)) + "@gmail.com"
print("Your email is: " + fullEmail)

randomCharacterOne = random.choice(characters)
randomCharacterTwo = random.choice(characters)
randomCharacterThree = random.choice(characters)
randomCharacterGroup = randomCharacterOne + randomCharacterTwo + randomCharacterThree

randomSymbolOne = random.choice(symbols)
randomSymbolTwo = random.choice(symbols)
randomSymbolGroup = randomSymbolOne + randomSymbolTwo

randomWord = random.choice(words)

password = str(len(name)) + randomCharacterGroup + randomSymbolGroup + randomWord
print(f"Your password is: {password}")
