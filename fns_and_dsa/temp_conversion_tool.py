FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
degree_symbol = "\u00B0"

def validate_temperature(input_value):
  try:
    return float(input_value)
  except:
    raise ValueError('Invalid temperature. Please enter a numeric value.')
  
def validate_unit(input_value):
  unit = input_value.strip().lower()
  if unit in ('c', 'f'):
    return unit
  else:
    raise ValueError("Invalid temperature scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

def convert_to_celsius(fahrenheit):
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
  return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

if __name__ == "__main__":
  try:
    tem_value = input("Enter the temperature to be converted: ")
    temperature = validate_temperature(tem_value)

    check = input('Is this temperature in Celsius or Fahrenheit? (C/F): ')
    unit = validate_unit(check)


    if unit == 'c':
      print(f'{temperature}{degree_symbol}C is {convert_to_fahrenheit(temperature)}{degree_symbol}F')
    elif unit == 'f':
      print(f'{temperature}{degree_symbol}F is {convert_to_celsius(temperature)}{degree_symbol}C')
    else:
      raise ValueError("Invalid temperature. Please enter a numeric value.")
  except ValueError as e:
    print(f'Error: {e}')