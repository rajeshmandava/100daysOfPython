from base64 import encode
from operator import index
from turtle import position


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def decrypt(text,shift):
  decoded_text = ""
  for letter in text:
    position = alphabet.index(letter)
    old_position = position - shift
    old_letter = alphabet[old_position]
    decoded_text += old_letter
  print(decoded_text)

def encrypt(text, shift):
  encoded_text=""
  for letter in text:
    position = alphabet.index(letter)
    new_position = position + shift
    new_letter = alphabet[new_position]
    encoded_text += new_letter

  print(encoded_text)



if direction == "encode":
  encrypt(text, shift)
elif direction == "decode":
  decrypt(text, shift)  
