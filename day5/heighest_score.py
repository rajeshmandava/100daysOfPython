scores = input("Enter the scores of the students").split()

for s in range(0,len(scores)):
  scores[s] = int(scores[s])

max = -1
for s in scores:
  if s>max:
    max = s

print(s)
