import random
import os
guessWord = []
myWord = ["peter", "lois", "chris", "meg", "stewie", "brian", "vinny", "joe", "quagmire", "cleveland", "mort", "herbert"]
theWord = random.choice(myWord)
misses = 0
theWord = list(theWord)

frameList = [
'''
   +---+
       |
       |
       |
       |
      ===''','''
   +---+
   O   |
       |
       |
       |
      ===''','''
   +---+
   O   |
   |   |
       |
       |
      ===''','''
   +---+
   O   |
  /|   |
       |
       |
      ===''','''
   +---+
   O   |
  /|\\  |
       | 
       |
      ===''','''
   +---+
   O   |
  /|\\  |
  /    |   
       |
      ===''','''
   +---+
   O   |
  /|\\  |
  / \\  |   
       |
      ==='''
]

while misses < 7:
  print(frameList[misses])
  guess = input("Guess a letter: ")
  if guess in theWord:
    theWord.append(guess)
    print("That letter is in the word")
  else:
    misses = misses + 1
    print("That letter is not in the word")

for a in theWord:
  guessWord.append("_")

choice = input("Type a word: ")
if choice == theWord:
  print("It's a match!")
else:
  print("Not a match")
letter = input("Type a letter: ")
if letter in theWord:
  print("Letter is in the word, nice job!")
else:
  print("Letter is not in the word")

count = 0
for s in theWord:
  if s == letter:
    print(count)
  count += 1

print(guessWord)