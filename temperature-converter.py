def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def temperature_conversion():
    print("Select a temperature conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    option = input("Enter the option number: ")

    if option == "1":
        celsius = float(input("Enter the temperature in Celsius: "))
        print(f"{celsius}°C is {celsius_to_fahrenheit(celsius)}°F")
    elif option == "2":
        celsius = float(input("Enter the temperature in Celsius: "))
        print(f"{celsius}°C is {celsius_to_kelvin(celsius)}K")
    else:
        print("Invalid option.")
