
'''
I am making my own example for loop base on the topic
'''


print(" while loop")

count = 1

while count <= 5:
    print(count)
    count += 1

print("========================================")

# BREAK with while loop
print("BREAK with while loop")

count = 1

while count <= 5:
    if count == 3:
        break
    print(count)
    count += 1

print("========================================")

# CONTINUE with while loop
print("CONTINUE with while loop")

count = 0

while count < 5:
    count += 1
    if count == 3:
        continue      # skips 3
    print(count)

print("========================================")

# ELSE with while loop
print("ELSE with while loop")

count = 1

while count <= 5:
    print(count)
    count += 1
else:
    print("Loop finished successfully!")

print("========================================")

# BREAK with ELSE
print("BREAK with ELSE")

count = 1

while count <= 5:
    if count == 3:
        print("Loop stopped!")
        break
    print(count)
    count += 1
else:
    print("Loop finished successfully!")

print("========================================")

# PASSWORD VALIDATION using while loop
print("PASSWORD VALIDATION")

password = ""

while password != "secret123":
    password = input("Enter password: ")

    if password != "secret123":
        print("Wrong! Try again.")

print("Access granted!")

print("========================================")