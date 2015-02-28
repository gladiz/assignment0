mixed_list = [256,250,'kigali', 254, 'kampala', 'nairobi']

city_code =[]
cities = []

print "before loop"

for item in mixed_list:
    if type(item) == int:
        city_code.append(item)
    elif type(item)==str:
        cities.append(item)

print "after loop"
print mixed_list
print city_code
print cities

