def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    while True:
        date_input = input("Date: ").strip()
        try:
            if "/" in date_input:
                month, day, year = date_input.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
        except ValueError:
            pass
        try:
            if "," in date_input:
                month_day, year = date_input.split(",")
                year = int(year.strip())
                parts = month_day.strip().split()
                if len(parts) == 2:
                    month_str, day = parts
                    day = int(day)
                    if month_str in months and 1 <= day <= 31:
                        month = months.index(month_str) + 1
                        print(f"{year:04d}-{month:02d}-{day:02d}")
                        break
        except ValueError:
            pass
        continue
if __name__ == "__main__":
    main()
