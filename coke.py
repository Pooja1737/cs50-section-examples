def main():
    amount_due = 50 
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        try:
            coin = int(input("Insert Coin: "))
        except ValueError:
            continue 
        if coin in [5, 10, 25]: 
            amount_due -= coin
    change = -amount_due if amount_due < 0 else 0
    print(f"Change Owed: {change}")
if __name__ == "__main__":
    main()
