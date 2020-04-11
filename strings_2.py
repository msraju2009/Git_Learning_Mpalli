# strings contain text 

my_string = "Hello, World !"
print(my_string)

string_with_quotes = 'Hello, it\'s me.'

string_with_double_quotes = "Hello, it's me."

another_quotes = 'Hello Mpalli, "You\'re amazing" everyday.'

print(string_with_quotes,string_with_double_quotes,another_quotes)

multiline_strings = """ Welcome,
My name is Madhu,
Welcome to Python programming 
"""

print(multiline_strings)

first_name = "chejerla"
middle_name = "MadhuSudhanaRaju"

print(first_name +"   "+ middle_name)

age = 34
#print("your age is " + age) # gives error

print("your age is " + str(age))

print(f"your age is {age} using format string ")

greeting = f"How are you doing {first_name} ?"

print(greeting)

print("How are you doing {} ?".format(first_name))

print("how are you doing ? {name}".format(name="Madhu"))

