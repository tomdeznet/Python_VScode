print("Hello, World!") # to print panta xwris keno apo tin parenthesi

x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")


myint = 1 # mono noumera
yourint = 5
float = 1.0 # mono dekadikous
mystring = "love" # mono lekseis h protaseis

mylist = []
mylist.append(10)
mylist.append(20)
mylist.append(30)

x1 = input()
for x1 in mylist:
    print(mylist[x1])



numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)

print(numbers[0])
print(numbers[1]) 
print(numbers[2])

strings.append("hello")
strings.append("world")

print(strings[0])
print(strings[1])

names.append(0)
names.append(1)
names.append(2)

second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

remainder = 7 % 3
print(remainder)


class1 = "geography"
time = 10
print("What time is the %s" % class1)
print("It's on %d pm" % time)


# %s ---> strings or numbers
# %d ---> integers
# %f ---> floating point numbers
# %.<number of digits>f ---> floating number with fixed amount of digits
# %x/%X ---> Integers in hex representation (lowercase/uppercase)
# sto telos anamesa panta %
name = "John"
age = 23
print("%s is %d years old and very smart" % (name,age))

result = 2.544
print("The results is %.2f" % result)


# You will need to write a format string which
# prints out the data using the following syntax:
# Hello John Doe. Your current balance is $53.44.

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%f."

print(format_string % data)

string = "test"
print(len(string)) # tha kanei print posous xaraktires exei to string
print(string.index("s")) # tha kanei print se poia thesi vriskete to s apo to prwto xaraktira
print(string.count("s")) # tha kanei print posa s uparxoun sto string
print(string[3:7]) # tha kanei print osoi xaraktires einai anamesa sto 3 kai sto 7
print(string.upper()) #ta kanei ola kefalaia
print(string.lower()) #ta kanei ola mikra

bstring = "Hello World!"
print(bstring.startswith("Hello")) # this will give you true
print(bstring.endswith("Hello")) # this will give you false

# this will give you a list with all the strings separated by space
teststring = "I Give up!"
teststring = teststring.split(" ")
print(teststring)


# if syntax
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick")


# if syntax with lists / use in before list
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")


statement = False
another_statement = True
if statement is True:
    pass
elif another_statement is True:
    pass
else:
    pass

x = 3
    if x == 3:
    print("x is equals three!")
else:
    print("x is not three")

print("What's your name?")
name = input()
print("So, your name is " + name)