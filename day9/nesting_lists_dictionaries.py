""" 
dict = 
{
  key  : [List],
  key2 : {Dict}
}
 """


#Nesting
from itertools import count


capitals = {
  "France" : "Paris",
  "Germany": "Berlin",
  "Sweden" : "Stockholm",
  "Norway" : "Oslo",
  "Finland" : "Helsinki"
}

# Nesting a List in a dictionary

travel_log = {
  "France" :  {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits":12},
  "Germany" : {"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits":10},

}

for country in travel_log:
  print(travel_log[country])

# Nesting Dictionary in a List

travel_log = [
  {
    "country" : "France",
    "cities_visited" : ["Paris", "Lille", "Dijon"],
    "total_visits":12
  },
  {
    "country" : "Germany",
    "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits" : 10
  }
]

print(travel_log)

# Coding Challenge

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def  add_new_country(country,no_of_visits,cities_visits):
  new_country = {
    "country" : country,
    "visits"  : no_of_visits,
    "cities" : cities_visits
  }
  travel_log.append(new_country)




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



