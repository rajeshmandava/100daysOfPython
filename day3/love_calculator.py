name1 = input("What is your name?")
name2 = input("What is their name?")

small_name1 = name1.lower()
small_name2 = name2.lower()

true_match = 0
love_match = 0

for x in "true":
  true_match += small_name1.count(x)
  true_match += small_name2.count(x)

for x in "love":
  love_match += small_name1.count(x)
  love_match += small_name2.count(x)

print(f"match % :{true_match}{love_match}")