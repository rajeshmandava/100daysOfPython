small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepporoni_small = 2
pepporoni_medium_large = 3
extra_cheese = 1

print("Welcome to Best Pizzas!")
size = input("What size do you want? S, M or L")
add_pepporoni = input("Do you want pepporoni? Y or N")
add_cheese = input("Do you want Cheese? Y or N")

bill =0

if size =="S":
  bill+=small_pizza
  if add_pepporoni == "Y":
    bill+=pepporoni_small
  if add_cheese == "Y":
    bill+=extra_cheese
elif size == "M":
  bill+=medium_pizza
  if add_pepporoni == "Y":
    bill+=pepporoni_medium_large
  if add_cheese == "Y":
    bill+=extra_cheese
else:
  bill+=large_pizza
  if add_pepporoni == "Y":
    bill+=pepporoni_medium_large
  if add_cheese == "Y":
    bill+=extra_cheese
print(f"Your total bill is {bill}")