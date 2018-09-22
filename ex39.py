"""
stuff = {'name':'Joy', 'age':33, 'height':6*12+2}

print(stuff['name'])
print(stuff['age'])
print(stuff['height'])

stuff['city'] = 'SF'
print(stuff['city'])

stuff[1] = 'wow'
stuff[2] = 'Neato'
print(stuff)

del stuff['city']
del stuff[1]
del stuff[2]
print(stuff)
"""

#mapping of states
states = {
  'Oregon':'OR',
  'Florida':'FL',
  'California':'CA',
  'New York':'NY',
  'Michigan':'MI'
}

#states and cities
cities = {
  'CA':'San Francisco',
  'MI':'Detroit',
  'FL':'Jacksonville'
}

#more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-'*10)
print("NY state has: ",cities['NY'])
print("OR state has: ",cities['OR'])

print('-'*10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

print('-'*10)
print("Michigan has: ",cities[states['Michigan']])
print("Florida has: ",cities[states['Florida']])

print('-'*10)
for state, abbrev in list(states.items()):
  print(f"{state} is abbreviated {abbrev}")

print('-'*10)
for abbrev, city in list(cities.items()):
  print(f"{abbrev} has the city {city}")

print('-'*10)
for state, abbrev in list(states.items()):
   print(f"{state} state is abbreviated {abbrev}")
   print(f"and has city {cities[abbrev]}")

print('-'*10)
state = states.get('Texas')

if not state:
  print("Sorry, no Texas.")


city = cities.get('TX', 'Does not exist.')
print(f"The city of the state TX is: {city}")
