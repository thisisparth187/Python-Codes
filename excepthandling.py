try:
    a = input("Enter an integer: ")
    a = int(a)
except ValueError:
    print("You didn't entered an integer!!")


try:
    a = int(input("Enter an integer: "))
    l = [10, 12, 23]
    print(l[a])
except ValueError:
    print("You didn't entered an integer!!")
except IndexError:
    print("Array is not that large!!!")
