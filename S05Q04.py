num = int(input("Enter a num "))
fib = 1
sum = 1
while sum<num and fib<num:
    sum = sum + fib
    fib = sum + fib
    if( sum == num or fib == num):
        print("Yes the number entered is a fibonacci number")
        
diff1 = abs(fib - num)
diff2 = abs(sum-num)

if diff1>diff2:
    ans = sum
else:
    ans = fib

print("the closest fibonaccci nunmber is ", ans )
