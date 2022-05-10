heights = input("Enter list of student heights:").split()
count =0
sum=0
for h in range(0,len(heights)):
  heights[h]=int(heights[h])

for h in heights:
  count+=1
  sum+=h
print(f"sum is {sum} and count is {count}")
average_height = int(sum/count)
print(f"The average height of the students is {average_height}")
