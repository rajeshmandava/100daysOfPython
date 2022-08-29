from random import random


word_list = ["advark", "baboon", "camel"]

rand_num = random.randint(0,2)
letter = input("Guess a letter: ")
random_word = word_list[rand_num]
for i in random_word:
  if i == letter:
    print("Right")
  else:
    print("Wrong")
