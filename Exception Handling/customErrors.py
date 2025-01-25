a = int(input("Enter number between 5 and 10:"))
if (a < 5 or a > 10):
    raise ValueError("That's not between 5 and 10")