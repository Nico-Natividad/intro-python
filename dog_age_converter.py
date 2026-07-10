print("=================================================")
print("----- Welcome to the Dog Age Converter ----")
print("=================================================")


dogagehum = int(input("Enter your dog's age in human years: "))
# I named the variable dogagehum to represent the dog's age in human years. I used the int() function to convert the user's input into an integer, as ages are typically represented as whole numbers. This allows for accurate calculations when converting to dog years.

dog_years = dogagehum * 7

'''
after calculating the dog's age in dog years, 
I stored the result in a variable called dog_years.
This variable will hold the value of the dog's age in dog years,
which is calculated by multiplying the dog's age in human years by 7. 
The multiplication factor of 7 is commonly used to estimate a dog's age
in relation to human years.
'''


print(f"Your dog is {dog_years} years old in dog years.")
#i used an f-string to format the output message, which allows me
# to easily include the value of the dog_years variable within the string. 
# This provides a clear and user-friendly way to display the result of the conversion 
# to the user.