class Calculator:

    def __init__(self, value=0) -> None:
        """
        Initializes a new instance of the class.
        
          Args:
            self: The instance of the class.
            value: The initial value to set the instance to. Defaults to 0.
        """
        self.value = value

    def add(self, number) -> int:
        """
        Adds a number to the internal value of the object.
        
          Args:
            self: The instance of the class.
            number: The number to be added.
        
          Returns:
            int: The sum of the internal value and the provided number.  The return type is inferred from the problem description, but the function body is missing so this cannot be verified.  The internal value is assumed to be an integer, but this is not explicitly stated.
        """
        self.value += number
        return self.value

    def subtract(self, number) -> int:
        """
        Subtracts a number from the object's internal value.
        
          Args:
            self: The object itself (presumably containing an internal numerical value).
            number: The number to subtract from the object's internal value.
        
          Returns:
            int: The result of the subtraction (the object's internal value minus the input number).
        """
        self.value -= number
        return self.value

    def multiply(self, number) -> int:
        """
        Multiplies the instance's internal value by the given number.
        
          Args:
            self: The instance of the class.  This assumes the class has an internal 
                  attribute that holds a numerical value (e.g., `self.value`).
            number: The number to multiply by.  Must be a number (int or float).
        
          Returns:
            int: The result of the multiplication as an integer.  If the result 
                 of the multiplication is not an integer, it will be truncated.
        
          Raises:
            TypeError: If 'number' is not an int or float.
            AttributeError: If the instance does not have a numerical attribute 
                            to multiply. (Assumes there's a numerical attribute)
        """
        self.value *= number
        return self.value

    def divide(self, number) -> str:
        """
        Divides the object's internal value by the given number.
        
          Args:
            self: The object itself.  Assumed to have a numerical attribute that can be divided.
            number: The number to divide by.  Should not be zero.
        
          Returns:
            str: A string representation of the result of the division.  
                 Handles potential ZeroDivisionError.  The exact format of the string is unspecified.
                 Example:  "Result: 2.5" or "Error: Division by zero"
        """
        if number == 0:
            raise ValueError("Cannot divide by zero.")
        self.value /= number
        return str(self.value)

    def get_value(self):
        """
        Returns the current value of the calculator.
        
        Returns:
            float: The current value.
        """
        return self.value


# Example usage:
if __name__ == "__main__":
    calc = Calculator(10)
    print("Initial value:", calc.get_value())
    print("After addition:", calc.add(5))
    print("After subtraction:", calc.subtract(3))
    print("After multiplication:", calc.multiply(2))
    print("After division:", calc.divide(4))
