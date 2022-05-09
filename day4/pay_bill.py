from operator import length_hint
import random
from unicodedata import name

name_list = ["Johnny", "Jacob", "Jimmy", "Joseph"]
length = length_hint(name_list)
index = random.randint(0,length-1)
print(f"{name_list[index]} is going to buy the meal today.")