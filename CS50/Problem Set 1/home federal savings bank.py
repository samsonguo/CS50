greeting = input("Greeting: ").strip().lower()
if greeting == "hello":
    print("$0")
elif "h" in greeting and "hello" not in greeting:
    print("$20")
else:
    print("$100")


""""
greeting = (input("Greeting: ")).lower().strip()
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
"""
