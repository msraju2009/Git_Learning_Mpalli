age = int(input("Enter your age "))
print("your age is {} ".format(age))

is_over_age = age >=18
is_under_age = age<18
is_twenty = age == 20




if is_over_age:
    print("you're over age ")
elif is_under_age:
    print("You're under age ")
elif is_twenty:
    print("your age is 20")
else:
    print(age)

can_learn_programming = age > 0 and age < 80
print(can_learn_programming)

usually_retired = age <18 or age > 65
print("usually retired {} ".format(usually_retired))

usually_working = age >=18 or age <=65 
print("usually working age is {} ".format(usually_working))

print(bool(35)) # True , most values evaluates to true


print(bool("")) # empty value means false 

