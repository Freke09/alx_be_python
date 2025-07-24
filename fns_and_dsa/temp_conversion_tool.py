FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

try:

    temperature_to_convert = float(input("Enter the temperature to convert: "))
    temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

    if temperature_type == 'C':
        print(f"{temperature_to_convert}°C is {convert_to_fahrenheit(temperature_to_convert)}°F")
    elif temperature_type == 'F':
        print(f"{temperature_to_convert}°F is {convert_to_celsius(temperature_to_convert)}°C")
    else:
        print("Invalid input. Please enter 'C' or 'F'.")

except ValueError:
    print("Invalid temperature. Please enter a numeric value.")