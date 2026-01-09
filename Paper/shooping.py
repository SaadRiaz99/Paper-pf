# Product List
products = [
    ["Surf", 100],
    ["Dettol", 150],
    ["Colgate", 80],
    ["Dove", 120],
    ["Lays", 50]
]

# Show Products
def show_products():
    print("\nAvailable Products:")
    for i in range(len(products)):
        print(i + 1, products[i][0], "- Rs.", products[i][1])

# Shopping Cart
def shopping_cart():
    cart = []
    total = 0

    while True:
        show_products()
        choice = int(input("\nSelect product number (1-5): "))
        qty = int(input("Enter quantity: "))

        item = products[choice - 1]
        cost = item[1] * qty
        total += cost

        cart.append(item[0])

        print(item[0], "added to cart.")
        print("Current Total: Rs.", total)

        more = input("Add more items? (y/n): ")
        if more.lower() != "y":
            break

    
    discount = 0
    if total >= 2000:
        discount = total * 0.02

    final_amount = total - discount

    print("\n------ BILL ------")
    print("Items:", cart)
    print("Total Amount: Rs.", total)
    print("Discount (2%): Rs.", discount)
    print("Payable Amount: Rs.", final_amount)
    print("Thank you for shopping 🛒")


shopping_cart()
