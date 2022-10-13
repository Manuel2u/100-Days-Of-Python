print("Welcome to tip calculator")
total = float(input("What was the total bill? $"))
num_of_pple = float(input("How many people to split the bill? "))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

each_person = round((total / num_of_pple) + (percentage / 100 * (total/num_of_pple)),1)

print(f"Each person should pay: ${each_person}")
