name = input("Enter your name: ")   
age  = int(input("Enter your age: "))


# Additional discounts and congrats message
if age < 12:
    print("Congrats! You are eligible for a child discount.")
elif age > 60:
    print("Congrats! You are eligible for a senior citizen discount.")
else:
    print("Sorry, no discount available for your age group.")


