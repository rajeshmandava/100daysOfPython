height = int(input("Enter your height in cms:"))

bill = 0
if height >= 120:
  print("allowed to ride rollercoster")
  age = int(input("Enter your age:"))
  if(age<12):
    bill = 5
  elif(age<=18):
    bill = 7
  else:
    bill = 12
  wants_photo = input("Do you want photo taken? Y or N.")
  if wants_photo=="Y":
    bill +=3
  print(f"your final bill is {bill}")


else:
  print("Not allowed to ride rollercoster")