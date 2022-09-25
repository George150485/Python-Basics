# Basic Data Types In Python
#int for integer
number  = 3
#float for decimal
decimal_number = 3.5
#str for string
name = "Hello"
#print the type
print(type(name))
print(type(decimal_number))
print(type(number))
#cast decimal to integer
print(int(decimal_number))
#cast int to float
print(float(number))
#cast string to number
numberString = "32"
print(str(numberString))
#print boolean
print(type(True))
#casting a boolean to interger & vice versa
print(int(True))
print(bool(1))
print(float(False))
print(float(True))
#Expression and Values
number  = 45+342+56 #Operands and operators '+'
print(number)
print(number/3)
#rounded division
print(number//3)
#String operations
name = "George" + " Tadros"
print(name)
print(name[3:6:2])
print(len(name))
name = name * 3
print(name)
#find a substring return the begining index of the
#substring
print(name.find("George"))
