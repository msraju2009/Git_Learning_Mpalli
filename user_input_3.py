name = input("Please enter your name  ")
# input always return string ,so it has to be 
# converted based on whatever type required
print("your name is {} ".format(name))
age = input("Enter your age ")
print("You lived for these months {} ".format(age*12))

print("You lived for these months {} ".format(int(age)*12))

print(f"You age in months is {int(age)*12} ")

