class Calculator:

    def __init__(self, value=0) -> None:
        self.value = value

    def add(self, number) -> int:
        self.value += number
        return self.value

    def subtract(self, number) -> int:
        self.value -= number
        return self.value

    def multiply(self, number) -> int:
        self.value *= number
        return self.value

    def divide(self, number) -> str:
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
