def stops():
    start = int (input("Enter starting value "))
    end  = int(input("Enter ending value "))
    fuel_consumed = int(input("Enter the fuel consumed "))

    mileage = (end - start)/ fuel_consumed

    initial_fuel = 50

    stops = int((560)/ (initial_fuel*mileage))

    print("You will have to make", stops, "stops if you have a fuel tank of 50L")

#main starts here
stops()

