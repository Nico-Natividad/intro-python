num = 8

if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is not positive.")    

#shorthand if-else statement
num = 8
print("even") if num % 2 == 0 else print("odd")

#nested if-else statement
num = 8
if num > 0:
    if num < 10:
        print("The number is positive and less than 10.")
        