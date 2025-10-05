greeting = input("Greeting: ")
cleaned = greeting.lstrip().lower()
if cleaned.startswith("hello"):
    print("$0")
elif cleaned.startswith("h"):
    print("$20")
else:
    print("$100")
