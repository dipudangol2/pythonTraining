def isPalindrome(x):
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    return str(x)[::-1] == str(x)


inputString = input("Enter the word or number:")
if isPalindrome(inputString):
    print("It is palindrome")
else:
    print("It is not palindrome")
