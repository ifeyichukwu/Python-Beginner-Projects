import math

print("You can convert from three units. \n Either from length or Weight or Temperature\n")

print("LENGTH: Meters -> Kilometers -> Miles -> Feet")

print("WEIGHT: Kilograms -> Ounces -> Pounds")

print("TEMPERATURE: Celsius -> Farenheit -> Kelvin")

def length_conversion():
    print("What would you like to convert from? \n")
    print("1. Meters to Kilometers")
    print("2. Meters to Miles")
    print("3. Meters to Feet")

    choice = int(input("Select conversion type: "))
    value = float(input("Enter the lenght in meters: "))

    if choice == 1:
        result = round(value * 0.001, 2)
        print(f"{value} meters is {result} kilometers")
    elif choice == 2:
        result = round(value * 0.000621, 2)
        print(f"{value} meters is {result} miles")
    elif choice == 3:
        result = round(value * 3.281, 2)
        print(f"{value} meters is {result} feet")
    else:
        print("Invalid choice!")

def weight_conversion():
    print("\nWeight Conversion:")
    print("What would you like to convert from? \n")
    print("1. Kilograms to Pounds")
    print("2. Kilograms to Ounces")

    choice = int(input("Select conversion type: "))
    value = float(input("Enter the weight in kilograms: "))

    if choice == 1:
        result = round(value * 2.205, 2)
        print(f"{value} kg is {result} pounds")
    elif choice == 2: 
        result = round(value * 35.374, 2)
        print(f"{value}kg is {result} ounces")
    else:
        print("Invalid choice!")

def temperature_conversion():
    print("\nTemperature Conversion: ")
    print("What would you like to convert from?")
    print("1. Celsius to Farenheit")
    print("2. Celcius to Kelvin")

    choice = int(input("Select conversion type: "))
    value = float(input("Enter the temperature in Celcius: "))

    if choice == 1:
        result = round((value *9/5) + 32, 2)
        print(f"{value}°C is {result}°F")
    elif choice == 2:
        result = round(value + 273.15, 2)
        print(f"{value}°C is {result}K")
    else:
        print("Invalid choice!")

while True:
    print("\nUnit Converter: Choose a Category")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")

    option = int(input("Enter your choice (1-3): "))

    if option == 1:
        length_conversion()
    elif option == 2:
        weight_conversion()
    elif option == 3:
        temperature_conversion()
    else:
        print("Invalid option! Please select 1, 2, or 3.")