num = int(input("Enter a number "))

max = min = single= two= three = 0
while num != 0:
    if num>max:
        max = num
    if num<min:
        min = num
    length = len(str(num))
    if length == 1:
        single += 1
    elif length == 2:
        two += 1
    elif length == 3:
        three += 1
    num = int(input("Enter another num"))

print("the max of all numbers was: ", max)
print("the min of all the numbers was: ", min)
print("there were ",single," one digit numbers")
print("there were ",two, " two digit numbers")
print("there were ",three, " three digit numbers")

