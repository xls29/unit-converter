def kilograms_to_pounds(kg):
    return kg * 2.20462

def grams_to_kilograms(grams):
    return grams / 1000

def weight_conversion():
    print("Select a weight conversion:")
    print("1. Kilograms to Pounds")
    print("2. Grams to Kilograms")
    option = input("Enter the option number: ")

    if option == "1":
        kg = float(input("Enter the weight in kilograms: "))
        print(f"{kg} kg is {kilograms_to_pounds(kg)} lbs")
    elif option == "2":
        grams = float(input("Enter the weight in grams: "))
        print(f"{grams} grams is {grams_to_kilograms(grams)} kg")
    else:
        print("Invalid option.")
