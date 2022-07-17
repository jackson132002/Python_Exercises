def do_1digit_oper(num):
    temp = num + 7
    print(temp%10)

def do_2digit_oper( num ):
    temp = num **5
    print(num % 10)

def do_3digit_ope(num):
    temp = int(input("Enter another number "))
    print(num + temp)



num1 = int(input("Enter a number "))

if num1<10:
    do_1digit_oper(num1)
if num1>=10 and num1<100:
    do_2digit_oper(num1)
elif num1>=100 and num1<1000:
    do_3digit_ope(num1)
