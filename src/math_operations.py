class MathOperations:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def power(self, a, b):
        return a**b

    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number.")
        return a**0.5

    def factorial(self, a):
        if a < 0:
            raise ValueError("Cannot calculate factorial of negative number.")
        if a == 0:
            return 1
        return a * self.factorial(a - 1)
