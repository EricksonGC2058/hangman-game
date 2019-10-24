import os
misses = 0
theWord = list("quagmire")
guessList = list("_______")

print(guessList)

frame = []

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
    index = 0
    for letter in theWord:
      if letter == guess:
        guessList[index] = guess
        print(guessList)
      index += 1
  else:
    misses = misses + 1

count = 0


if frame == frameList[6]:
  print("Game over")
  print(theWord)

print(guessList)