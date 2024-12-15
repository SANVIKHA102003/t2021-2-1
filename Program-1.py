class Calculator:
    def __init__(self, a: float, b: float, operation: str):#used float since python doesn't have double datatype
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        if self.operation == 'addition':
            return self.a + self.b
        elif self.operation == 'subtraction':
            return self.a - self.b
        elif self.operation == 'multiplication':
            return self.a * self.b
        elif self.operation == 'division':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Division by zero is not possible"
        else:
            return "Enter valid operation"


def main():
    a = float(input("Enter the first number (a): "))
    b = float(input("Enter the second number (b): "))
    operation = input("Enter the type of operation (addition, subtraction, multiplication, division): ")
    calculator = Calculator(a, b, operation)
    result = calculator.calculate()
    print(f"Result: {result}")
    
if __name__ == "__main__":
    main()
