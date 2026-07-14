cart = []


def header(text):
    print("----------------------")
    print(text)
    print('----------------------')

def menu():
    print("menu")
    print("1. View catalog")
    print("2. Search product")
    print("3 View Cart")

    print("q to quit")

def catalog():
    header("Our catalog")
    for prod in catalog:
        print(f'| {prod["id"]} | {prod["title"]} | {prod["price"]}')
    answer = input("Type ID to add (N close):")
    if answer.lower() =="n":
        return
    else:
        add_product_to_cart(answer)

def add_product_to_cart(prod_id):
    found =  False
    for prod in catalog:
        if str(prod["id"]) == str(prod_id):
            found = True
            cart.append(prod)
            print(f'{prod["title"]}added to cart')
            break
    if not found:
        print("error")

# SEARCH PRODUCT using for loop
print("SEARCH PRODUCT")

def search_product():
    text = input("Search Product: ").lower()
    found = False

    for prod in catalog:
        if text in prod["title"].lower():
            found = True

            print(f"Found: ID {prod['id']} | {prod['title'].ljust(15)} | ${prod['price']:.2f}")

            choice = input("Do you want to add this item to your cart? (y/n): ")

            if choice.lower() == "y":
                add_product_to_cart(prod["id"])

            break   # Stop searching after the first match

    if not found:
        print("Sorry, this item doesn't exist.")

print("========================================")

# VIEW CART using for loop
print("VIEW CART")

def view_cart():
    header("Your Cart")

    if not cart:
        print("Your cart is empty.")
    else:
        # Loop through every product in the cart
        for prod in cart:
            print(f"| {prod['id']} | {prod['title'].ljust(15)} | ${prod['price']:.2f} |")

print("========================================")



option = ""
while option != "q" and option != "Q":
    header("welcome to store")
    menu()

    option = input("Choose an option")
    if option =="1":
        print("menu")
        catalog()
    elif option == "2":
        print("Search product")
        search_product()
    elif option =="3":
        print("View cart")
        view_cart()
    elif option =="q" and option =="Q":
        
        print("good bye")
        break
    else:
        print("error")