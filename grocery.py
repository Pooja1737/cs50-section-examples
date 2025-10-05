def main():
    from collections import Counter
    items = []
    try:
        while True:
            item = input().strip().lower()
            if item:
                items.append(item)
    except EOFError:
        print() 
    counts = Counter(items)
    for item in sorted(counts):
        print(f"{counts[item]} {item.upper()}")
if __name__ == "__main__":
    main()
