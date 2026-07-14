# 1. Basic for loop
print("1. Basic for loop")

for x in range(2, 6):
    print(x)

print("========================================")

# 2. Using step
print("2. Using step")

for number in range(0, 10, 2):
    print(number)

print("========================================")

# 3. Looping through a list
print("3. Looping through a list")

fruits = ["Apple", "Banana", "Orange", "Mango"]

for fruit in fruits:
    print(fruit)

print("========================================")

# 4. Looping through a string
print("4. Looping through a string")

for letter in "NICO":
    print(letter)

print("========================================")

# 5. Using break
print("5. break statement")

for x in range(1, 11):
    if x == 6:
        break
    print(x)

print("========================================")

# 6. Using continue
print("6. continue statement")

for x in range(1, 11):
    if x == 6:
        continue
    print(x)

print("========================================")

# 7. Using else
print("7. else in for loop")

for x in range(1, 6):
    print(x)
else:
    print("Loop finished!")

print("========================================")

# 8. Nested for loop
print("8. Nested for loop")

for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row}, {col})", end=" ")
    print()

print("========================================")

# 9. Using enumerate()
print("9. enumerate()")

colors = ["Red", "Green", "Blue"]

for index, color in enumerate(colors):
    print(index, color)

print("========================================")

# 10. Multiplication Table
print("10. Multiplication Table of 5")

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

print("========================================")
print("========================================")

# 9. ENUMERATE() - Get the index and the value
print("9. enumerate()")

fruits = ["apple", "banana", "cherry"]

# Default index starts at 0
for index, fruit in enumerate(fruits):
    print(index, fruit)

print("========================================")

# Start the index at a different number
print("10. enumerate() with start")

for index, fruit in enumerate(fruits, start=4):
    print(f"{index}. {fruit}")

print("========================================")