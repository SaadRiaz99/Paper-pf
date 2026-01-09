products = {
    1 :{"name": "Apple", "price": 100},
    2 :{"name": "Banana", "price": 50},
    3 :{"name": "Orange", "price": 80},
    4 :{"name": "Grapes", "price": 120},
    5 :{"name": "Mango", "price": 150}
}

def add_to_cart():
    print("Available Products")
    for key,value in products.items():
        print(f"{key}. {value['name']} -- Rs.{value['price']}")

def shop():
    total = 0
    cart = []
    while True:
        add_to_cart()
        choice = int(input("Select product number (1-5): "))
        quantity = int(input("Enter quantity: "))
        item = products[choice]
        cost = item["price"] * quantity
        total += cost
        cart.append(item["name"])
        print(item["name"], "added to cart.")
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
    print("Thank you for shopping "
    )
shop()    