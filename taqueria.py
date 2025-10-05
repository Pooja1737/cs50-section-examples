def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    menu_lower = {item.lower(): price for item, price in menu.items()}
    total = 0.0
    try:
        while True:
            item = input("Item: ").strip().lower()
            if item in menu_lower:
                total += menu_lower[item]
                print(f"Total: ${total:.2f}")
    except EOFError:
        print()
        return
if __name__ == "__main__":
    main()
