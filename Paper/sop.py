produts = [
    ["Apple", 100],
    ["Banana", 50],
    ["Orange", 80],
    ["Grapes", 120],
    ["Mango", 150]
    ]


def addtocart():
    print("\nAvailable Products:")
    for i in range(len(produts)):
        print(i + 1 , products[i][0], "--Rs." , produts[i][1])
def shopp():
    cart = [
    ]       
    total = 0
    while True:
        addtocart()
        chosise = int(input("Select product number (1-5): "))
        quantity = int(input("Enter quantity: "))
        item = products[chosise - 1]
        cost = item[1] * quantity
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
    print("Thank you for shopping "
    )