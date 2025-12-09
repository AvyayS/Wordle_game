import random
import math

with open("wordlelist.txt", "r") as somefile:
  random_words = somefile.read().split()
  #random_words = content.split()

def start(enter):
  enter = input("Welcome to WORLDLE (type START to play!): ")
  if enter.lower() == "start":
    print("Thanks for choosing to play WORLDLE!")
  else:
      enter = input("Welcome to WORLDLE (type START to play!): ")
random_index = random.randrange(0, len(random_words)-1)
random_word = random_words[random_index]
start("start")
guesses_amt = 6
feedback_list = []
while guesses_amt >= 1:
  guess = input("Guess the randomly generated 5-letter word: ")
  if guess not in random_words:
    print("Your guess is INVALID")
    guesses_amt = guesses_amt
  elif guess in random_words:
    for i in range(5):
      if guess[i] == random_word[i]:
        feedback_list.append(guess[i].upper())
      elif guess[i] != random_word[i] and guess[i] in random_word:
        feedback_list.append(guess[i].lower())
      elif guess[i] not in random_word:
        feedback_list.append("_")
    feedback_string = " ".join(feedback_list)
    print(feedback_string)
    if guess == random_word:
      print("GAME OVER")
      print("You won!")
      guesses_amt = -1
    feedback_list = []
    guesses_amt = guesses_amt - 1
if guesses_amt <= 0 and guess != random_word:
  print("GAME OVER")
  print("You lost...")
  print("The word was:", random_word)
