num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number"))

if num1<100:
    print(num1, "is a 2 digit number ")
elif num1>=100 and num1<1000:
    print(num1, "is a 3 digit number")
elif num1>=1000:
    print(num1)

if num2<100:
    print(num2, "is a 2 digit number ")

elif num2>=100 and num2<1000:
    print(num2, "is a 3 digit number ")

elif num2>=1000:
    print(num2)