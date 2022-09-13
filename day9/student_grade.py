from ast import And


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for name in student_scores:
  score = student_scores[name]
  str = ""
  if score >=91:
    str = "Outstanding"
  elif score >= 81 and score <=90:
    str = "Exceeds Expectations"
  elif score >=71 and score <= 80:
    str = "Acceptable"
  else:
    str = "Fail"
  student_grades[name] = str


    

# 🚨 Don't change the code below 👇
print(student_grades)





