def table(num):
    count = 1
    while(count <= 10):
        print(num, "X", count, "=", num*count)
        count += 1

inp = int(input("enter a num"))
table(inp)