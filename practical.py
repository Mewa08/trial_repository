orders_list = []

def add_order():
    print("\nAdd Order")

    try:
        order_id = int(input("Enter Order ID: "))
    except ValueError:
        print("Invalid ID")
        return

    for order in orders_list:
        if order["id"] == order_id:
            print("Order ID already exists")
            return

    name = input("Enter Customer Name: ")
    item = input("Enter Food Item: ")

    try:
        amount = float(input("Enter Amount: "))
        if amount < 0:
            print("Amount cannot be negative")
            return
    except ValueError:
        print("Invalid amount")
        return

    order = {
        "id": order_id,
        "name": name,
        "item": item,
        "amount": amount,
        "status": "Pending"
    }

    orders_list.append(order)
    print("Order added successfully")

def view_orders():
    print("\nView Orders")

    if len(orders_list) == 0:
        print("No orders available")
        return

    print("\nID   Name        Item        Amount   Status")
    print("-----------------------------------------------")

    for order in orders_list:
        print(f"{order['id']}    {order['name']}    {order['item']}    {order['amount']}    {order['status']}")

def search_order():
    print("\nSearch Order")

    try:
        search_id = int(input("Enter Order ID: "))
    except ValueError:
        print("Invalid ID")
        return

    for order in orders_list:
        if order["id"] == search_id:
            print(order)
            return

    print("Order not found")

def update_status():
    print("\nUpdate Status")

    try:
        search_id = int(input("Enter Order ID: "))
    except ValueError:
        print("Invalid ID")
        return

    for order in orders_list:
        if order["id"] == search_id:
            print("1. Pending")
            print("2. Completed")

            choice = input("Enter choice: ")

            if choice == "1":
                order["status"] = "Pending"
            elif choice == "2":
                order["status"] = "Completed"
            else:
                print("Invalid option")
                return

            print("Status updated")
            return

    print("Order not found")

def total_sales():
    print("\nTotal Sales")

    total = 0
    for order in orders_list:
        total += order["amount"]

    print("Total Sales =", total)

def count_completed():
    print("\nCompleted Orders")

    count = 0
    for order in orders_list:
        if order["status"] == "Completed":
            count += 1

    print("Completed Orders =", count)

def checkout():
    print("\nCheckout Order")

    try:
        order_id = int(input("Enter Order ID: "))
    except ValueError:
        print("Invalid ID")
        return

    for order in orders_list:
        if order["id"] == order_id:
            if order["status"] == "Completed":
                print("Already completed")
            else:
                order["status"] = "Completed"
                print("Order checked out")
            return

    print("Order not found")

def main():
    while True:
        print("\n--- RESTAURANT SYSTEM ---")
        print("1. Add Order")
        print("2. View Orders")
        print("3. Search Order")
        print("4. Update Order Status")
        print("5. Calculate Total Sales")
        print("6. Count Completed Orders")
        print("7. Checkout")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_order()
        elif choice == "2":
            view_orders()
        elif choice == "3":
            search_order()
        elif choice == "4":
            update_status()
        elif choice == "5":
            total_sales()
        elif choice == "6":
            count_completed()
        elif choice == "7":
            checkout()
        elif choice == "8":
            print("Goodbye")
            break
        else:
            print("Invalid choice")

main()