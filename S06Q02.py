sum = 0
waste = 0
six =0
four = 0
current = 0
balls = 0
sum = sum + int(current)
while current != "":
    balls += 1
    current = input("Enter runs ")
    if(current == '4'):
        four += 1
    if(current =='6'):
        six += 1
    if current == ".":
        waste += 1
    elif current == "":
        break;
    else:
        sum += int(current)

print("total runs scored ", sum)
print("total balls played ", balls)
print("balls wasted ", waste)
print("number of fours ", four)
print("number of sixes ", six)
print("strike rate ", sum/balls)


    
