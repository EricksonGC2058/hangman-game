import random
import os
guessWord = []
myWord = ["peter", "lois", "chris", "meg", "stewie", "brian", "vinny", "joe", "quagmire", "cleveland", "mort", "herbert"]
myList = list(myWord)
random.choice(myWord)

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
  /|\\   |
       | 
       |
      ===''','''
   +---+
   O   |
  /|\\   |
  /    |   
       |
      ===''','''
   +---+
   O   |
  /|\\   |
  / \\   |   
       |
      ==='''
]

for a in myWord:
  guessWord.append("_")

choice = input("Type a word: ")
if choice == myWord:
  print("It's a match!")
else:
  print("Not a match")
letter = input("Type a letter: ")
if letter in myWord:
  print("Letter is in the word, nice job!")
else:
  print("Letter is not in the word")

count = 0
for s in myWord:
  if s == letter:
    print(count)
  count += 1

print(guessWord)