class Calculator:
    def __init__(self):
        self.numbers = []
        self.num_count = None

    def input_numbers(self):
        self.num_count = int(input("How many numbers ? :"))
        for i in range(self.num_count):
            input_num = float(input(f"Enter number {i+1} : "))
            if input_num % 1 == 0:
                self.numbers.append(int(input_num))
            else:
                self.numbers.append(input_num)
        print(self.numbers)

    def add(self):
        result = 0
        for number in self.numbers:
            result += number
        return result

    def subtract(self):
        result = self.numbers[0]
        for number in self.numbers[1:]:
            result -= number
        return result

    def multiply(self):
        result = 1
        for number in self.numbers:
            result *= number
        return result

    def divide(self):
        try:
            print(
                f"Quotient : {self.numbers[0] // self.numbers[1]} Remainder : {self.numbers[0] % self.numbers[1]}"
            )
        except ZeroDivisionError:
            print(ZeroDivisionError)

    def menu(self):
        choice = int(
            input(
                """Enter your choice
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Exit
"""
            )
        )
        if choice == 1:
            print(f"Addition is {self.add()}")
        elif choice == 2:
            print(f"Subtraction is {self.subtract()}")
        elif choice == 3:
            print(f"Multiplication is {self.multiply()}")
        elif choice == 4:
            self.divide()
        else:
            print("Wrong choice!!!")


print("Simple Calculator using python")
while True:
    calc = Calculator()
    calc.input_numbers()
    calc.menu()
    choice = input("Do you want to continue?(y/n)")
    if choice=='y' or choice=='Y':
        pass
    else:
        break
    
