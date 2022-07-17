capacity = 900
current = int(input("Enter the current level of ethanol:"))

if current > (0.8* capacity):
    print("Close the valve")
elif current < (0.2 * capacity):
    print("Buy more liquid")
