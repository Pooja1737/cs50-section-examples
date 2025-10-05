def main():
    time_str = input("Time: ")
    hours = convert(time_str)
    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")
def convert(time):
    h, m = time.split(":")
    h = int(h)
    m = int(m)
    return h + m / 60
if __name__ == "__main__":
    main()
