height = int(input("Enter your height in cms:"))
age = int(input("Enter your age:"))
if height >= 120:
  print("allowed to ride rollercoster")
  if(age<12):
    print("Pay $5")
  elif(age<=18):
    print("pay $7")
  else:
    print("pay $10")
else:
  print("Not allowed to ride rollercoster")