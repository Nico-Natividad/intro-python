print('hello world from python!')
print(2)
print(5+3)

'''
this is a multi-line comment. I used it to explain the purpose
 of the code and provide additional context. Multi-line comments
   are useful for documenting code and making it easier to understand 
   for others (or for myself in the future).

'''

#variable and concatenation
name = "John"
age = 25
male = True
print(name,age)
print("My name is " + name + " and I am " + str(age) + " years old.")

#f strings
print(f"My name is {name} and I am {age} years old.")
#multi line f strings
print(f"""My name is {name} and I am {age} years old.""")


#type of function
print(type(name))
print(type(age))
print(type(male))

#casting changing data types
print(20,str(age))


#input function
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
print(user_name)
print(user_age)
print(f"Hello {user_name}, you are {user_age} years old.")