#list are created with squre backets

my_list = [1, 2, 3, 4, 5]
print(my_list)

# mixed list
mixed_list = [1, "two", 3.0, True]
print(mixed_list)

#accessing items by index   
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana

numbers = [10, 20, 30, 40, 50]
print(numbers[2:5])  # Output: [30, 40, 50]
print(numbers[:4])  # Output: [10, 20, 30, 40]
print(numbers[4:5])  # Output: [50]
print(numbers[-3:])  # Output: [30, 40, 50]

#modifying items in a list
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

#add items to a list
fruits.append("orange")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

#delete items from a list
fruits.remove("apple")
print(fruits)  # Output: ['blueberry', 'cherry', 'orange']

#inserting items into a list
fruits.insert(1, "kiwi")
print(fruits)  # Output: ['blueberry', 'kiwi', 'cherry', 'orange']


#loop in a list
for fruit in fruits:
    print(fruit)
#length in a list
print(len(fruits))  # Output: 4



