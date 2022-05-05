print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $:"))

tip = int(input("What percentage would like to tip 10, 12 or 15?:"))
tip_cal = (bill * tip)/100;
total_bill = tip_cal + bill
split = int(input("How many people will split the bill?:"))
single_bill = round(total_bill/split,2)
single_bill = "{:.2f}".format(single_bill)
print(f"Each person should pay : {single_bill}")