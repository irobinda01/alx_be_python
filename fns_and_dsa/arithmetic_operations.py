def perform_operation(num1, num2, operation):
  if(operation == "add"):
    return num1 + num2
  elif(operation == "subtract"):
    return num1 - num2
  elif(operation == "multiply"):
    return num1 * num2
  elif(operation == "divide"):
    try:
      return num1 / num2
    except ZeroDivisionError:
      return f"The value {num2} is zero, so zero division error occured.."
  else:
    return "Invalid operation"