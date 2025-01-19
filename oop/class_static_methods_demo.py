class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers, referencing a class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Example Usage
# if __name__ == "__main__":
#     # Using the static method
#     result_add = Calculator.add(5, 3)
#     print(f"The sum is: {result_add}")

#     # Using the class method
#     result_multiply = Calculator.multiply(5, 3)
#     print(f"The product is: {result_multiply}")
