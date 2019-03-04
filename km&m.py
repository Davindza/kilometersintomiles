print ("Hello!!! This is a program that converts units. More specifically, kilometers into miles")

while True:
    print("Enter a number of kilometers.")

    km = input("Kilometers: ")

    km = float(km.replace(",", "."))

    miles = km * 0.621371

    print("{0} kilometers is {1} miles.".format(km, miles))

    choice = input("Would you like to do other conversion (y/n):")

    if choice.lower() !="y" and choice.lower() !="yes":
        break