
# Simple Function
from unittest import result


def greet():
  print("Hello world")
  print("Today is Tuesday")
  print("I am excited to code")

greet()

# Function that allows input

def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How is your day {name}")

greet_with_name("Rajesh")

# Function with more than 1 parameters
def add(a,b):
  result = a+b
  print(result)

add(3,4)

def greet_with(name, location):
  print(f"Hello  {name}")
  print(f"What is it like in {location}")

name = "Jack Reacher"
location ="Stockholm"
greet_with(name, location)