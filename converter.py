def menu():
    print("Welcome to the Unit Converter")
    print("Select an option:")
    print("1. Convert Length")
    print("2. Convert Temperature")
    print("3. Convert Weight")
    print("4. Exit")
    option = input("Enter the option number: ")
    return option

def meters_to_kilometers(meters):
    return meters / 1000

def inches_to_centimeters(inches):
    return inches * 2.54

def length_conversion():
    print("Select a length conversion:")
    print("1. Meters to Kilometers")
    print("2. Inches to Centimeters")
    option = input("Enter the option number: ")
    
    if option == "1":
        meters = float(input("Enter the amount in meters: "))
        print(f"{meters} meters are {meters_to_kilometers(meters)} kilometers")
    elif option == "2":
        inches = float(input("Enter the amount in inches: "))
        print(f"{inches} inches are {inches_to_centimeters(inches)} centimeters")
    else:
        print("Invalid option.")

def main():
    while True:
        option = menu()
        
        if option == "1":
            print("\n--- Length Conversion ---")
            length_conversion()
        elif option == "2":
            print("\n--- Temperature Conversion ---")
        elif option == "3":
            print("\n--- Weight Conversion ---")
        elif option == "4":
            print("Thank you for using the Unit Converter. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()


