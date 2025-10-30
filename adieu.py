def main():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break
    farewell = "Adieu, adieu, to "
    if len(names) == 1:
        farewell += names[0]
    elif len(names) == 2:
        farewell += f"{names[0]} and {names[1]}"
    else:
        farewell += ", ".join(names[:-1]) + f", and {names[-1]}"
    print(farewell)
if __name__ == "__main__":
    main()
