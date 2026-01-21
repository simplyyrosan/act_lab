def get_valid_choice(prompt, options):
    """Keep asking until user enters a valid option key from options dict."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice
        print("Invalid choice, please try again.")


def get_yes_no(prompt):
    """Validate that user only enters 'y' or 'n'."""
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("y", "n"):
            return ans
        print("Please enter only 'y' or 'n'.")


def main():
    # Menus with prices
    sizes = {
        "s": ("Small", 200),
        "m": ("Medium", 300),
        "l": ("Large", 400)
    }

    sauces = {
        "t": ("Tomato", 0),
        "p": ("Pesto", 30),
        "w": ("White garlic", 40)
    }

    cheeses = {
        "r": ("Regular cheese", 0),
        "e": ("Extra cheese", 50),
        "n": ("No cheese", 0)
    }

    toppings = {
        "p": ("Pepperoni", 40),
        "m": ("Mushroom", 30),
        "o": ("Olives", 25),
        "c": ("Corn", 20)
    }

    other_items = {
        "1": ("Coke", 50),
        "2": ("Water", 20),
        "3": ("Ice cream", 60)
    }

    total = 0
    order_details = []

    print("==== Welcome to Python Pizza ====")

    # 1) Size
    print("\nChoose pizza size:")
    for k, (name, price) in sizes.items():
        print(f"{k}) {name} - ₹{price}")
    size_choice = get_valid_choice("Enter size (s/m/l): ", sizes)
    size_name, size_price = sizes[size_choice]
    total += size_price
    order_details.append(f"Size: {size_name} (₹{size_price})")

    # 2) Sauce
    print("\nChoose sauce:")
    for k, (name, price) in sauces.items():
        extra = f" (+₹{price})" if price > 0 else ""
        print(f"{k}) {name}{extra}")
    sauce_choice = get_valid_choice("Enter sauce: ", sauces)
    sauce_name, sauce_price = sauces[sauce_choice]
    total += sauce_price
    order_details.append(f"Sauce: {sauce_name} (₹{sauce_price})")

    # 3) Cheese
    print("\nChoose cheese:")
    for k, (name, price) in cheeses.items():
        extra = f" (+₹{price})" if price > 0 else ""
        print(f"{k}) {name}{extra}")
    cheese_choice = get_valid_choice("Enter cheese: ", cheeses)
    cheese_name, cheese_price = cheeses[cheese_choice]
    total += cheese_price
    order_details.append(f"Cheese: {cheese_name} (₹{cheese_price})")

    # 4) Toppings (yes/no for each)
    print("\nChoose toppings (y/n):")
    for code, (name, price) in toppings.items():
        ans = get_yes_no(f"Add {name} for ₹{price}? (y/n): ")
        if ans == "y":
            total += price
            order_details.append(f"Topping: {name} (₹{price})")

    # 5) Optional: other items (drinks/desserts)
    add_other = get_yes_no("\nDo you want to add drinks or desserts? (y/n): ")
    if add_other == "y":
        while True:
            print("\nOther items:")
            for k, (name, price) in other_items.items():
                print(f"{k}) {name} - ₹{price}")
            print("0) Done adding items")

            item_choice = input("Choose item number (or 0 to finish): ").strip()
            if item_choice == "0":
                break
            elif item_choice in other_items:
                name, price = other_items[item_choice]
                total += price
                order_details.append(f"Extra item: {name} (₹{price})")
                print(f"Added {name}. Current total: ₹{total}")
            else:
                print("Invalid choice, please try again.")

    # 6) Final confirmation
    print("\n===== Your Order =====")
    for line in order_details:
        print(line)
    print(f"Total cost: ₹{total}")

    confirm = get_yes_no("Confirm order? (y/n): ")
    if confirm == "y":
        print("Order confirmed! Thank you.")
    else:
        print("Order cancelled.")

if __name__ == "__main__":
    main()
