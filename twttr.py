def main():
    text = input("Input: ")
    vowels = "AEIOUaeiou"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    print(f"Output: {result}")
if __name__ == "__main__":
    main()
