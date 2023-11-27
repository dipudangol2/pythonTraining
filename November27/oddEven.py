def isEven(number: int)->bool:
    return number % 2 == 0


number = int(input("Enter Number : "))
if isEven(number):
    print("Number is even.")
else:
    print("Number is odd.")
