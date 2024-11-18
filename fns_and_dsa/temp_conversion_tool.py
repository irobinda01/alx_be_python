FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
degree_symbol = "\u00B0"

def convert_to_celsius(fahrenheit):
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
  return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

if __name__ == "__main__":
  try:
    check = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').capitalize()

    if check == 'C':
      tem = float(input("Enter the temperature to be converted: "))
      print(f'{tem}{degree_symbol}C is {convert_to_fahrenheit(tem)}{degree_symbol}F')
    elif check == 'F':
      tem = float(input("Enter the temperature to be converted: "))
      print(f'{tem}{degree_symbol}F is {convert_to_celsius(tem)}{degree_symbol}C')
    else:
      raise ValueError("Invalid temperature scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
  except ValueError as e:
    print(f'Error: {e}')