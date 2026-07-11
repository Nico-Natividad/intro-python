
#creating my own list and other syntax

colors = ["red", "green", "blue", "yellow", "orange"]
print(colors)
print(colors[0])  
print(colors[-1])  
colors.pop(3)
print(colors)
colors.remove("green")
print(colors)

print(len(colors))

colors.append("purple")
print(colors)

colors.insert(1, "pink")
print(colors)


#creating a dictionary and other syntax

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person)
print(person["name"])
print(person["age"])
print(person["city"])

person["age"] = 31
print(person)


person.get("name")
print(person.get("name"))

person.pop("city")
print(person)

print(len(person))

person["country"] = "USA"
print(person)
