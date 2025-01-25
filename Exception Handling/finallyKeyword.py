def func():
    try:
        a = int(input("Enter an integer:"))
        return 1
    except ValueError:
        print("That wasnt an integer!!")
        return 0
    finally:
        print("Going outside function...")

    print("Is this line printed??")

func()