programming_dictionary = { 
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop" : "The action of doing something over and over again"
}

print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])
print(programming_dictionary["Loop"])
# print(programming_dictionary["test_not_found"]) KeyError
# print(programming_dictionary[function]) NameError: name 'function' is not defined

# Adding new elements into dictionary

programming_dictionary["item"] = "The action of doing something over and over again"
print(programming_dictionary["item"])
# programming_dictionary = {} clearing the dictionary with empty
print(programming_dictionary)

# Edit an item in dictionary
programming_dictionary["Bug"] = "New bug value added into the dictionary"
print(programming_dictionary)

# Loop through the dictionary

for key in programming_dictionary:
  print(programming_dictionary[key])