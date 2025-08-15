total_bill = float(input("Enter the total hotel bill amount: "))
num_people = int(input("Enter the number of people: "))

if num_people > 2:
    print("Congrats! You are eligible for a group discount.")
elif num_people == 2:
    print("You are eligible for a couple's discount.")
elif num_people == 1:
    print("Sorry, no discount available for a single person.")
else:
    print("Invalid number of people entered.")
