class Calculator:
    def add(self, a, b, c=None):
        """Add two or three numbers."""
        if c is not None:
            return a + b + c  
        else:
            return a + b     

if __name__ == "__main__":
    calculator = Calculator()

    result1 = calculator.add(5, 10)
    print("Sum of 5 and 10 is:", result1)

    result2 = calculator.add(1, 2, 3)
    print("Sum of 1, 2, and 3 is:", result2)