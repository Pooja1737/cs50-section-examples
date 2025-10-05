def main():
    while True:
        fraction = input("Fraction: ").strip()
        try:
            x_str, y_str = fraction.split("/")
            x = int(x_str)
            y = int(y_str)
            if x < 0 or y <= 0 or x > y:
                continue
            percent = round((x / y) * 100)
            if percent <= 1:
                print("E")
            elif percent >= 99:
                print("F")
            else:
                print(f"{percent}%")
            break 
        except (ValueError, ZeroDivisionError):
            continue  
if __name__ == "__main__":
    main()
