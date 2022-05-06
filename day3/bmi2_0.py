height = float(input("Enter your height in meters:"))
weight = float(input("Enter your weight in Kg:"))

bmi = weight/(height*height)
print(round(bmi))
if bmi<=18.5:
  print("you are under weight")
elif bmi>18.5 and bmi<=25:
  print("you are normal weight")
elif bmi>25 and bmi <=30:
  print("you are overweight")
elif bmi>30 and bmi<35:
  print("you are obese")
else:
  print("you are clinically obese")