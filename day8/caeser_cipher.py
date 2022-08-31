from base64 import encode
from operator import index
from turtle import position


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caeser(text, shift, direction):
  final_text = ""
  if direction == "encode":
    for letter in text:
      position = alphabet.index(letter)
      new_position = position + shift
      new_letter = alphabet[new_position]
      final_text += new_letter
    
  elif direction == "decode":
    for letter in text:
      position = alphabet.index(letter)
      old_position = position - shift
      old_letter = alphabet[old_position]
      final_text += old_letter
  print(final_text)

caeser(text, shift, direction)