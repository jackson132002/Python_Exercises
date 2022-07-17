


english = int(input("Enter english marks "))
science = int(input("Enter science marks "))
maths = int(input("Enter mathematics marks "))
english_max = 80
science_max = 90
maths_max = 100
total_max = english_max+science_max+ maths_max
obtained = english+science+maths

percentage = (obtained/total_max)*100

if percentage>= 90:
    print("First Class")
elif percentage<90 and percentage>=75:
    print("Second Class")
elif percentage<75 and percentage>35:
    print("average")
elif percentage<=35:
    print("Fail")

