#String data type

#literal assignment
first='Rhea'
last='Tulod'

# print(type(first))
# print(type(first)==str)
# print(isinstance(first, str))

#constructor function
# pizza =str('Pepperoni')
# print(type(pizza))
# print(type(pizza)==str)
# print(isinstance(pizza,str))

#Concatenation
fullname = first +""+ last
print(fullname)

fullname += "!"
print(fullname)

#Casting a number to a string
decade = str(1997)
print(type(decade))
print(decade)

statement ="I like love song music from the" + decade + "s."
print(statement)

#Multiple lines
multiline = '''
Hey, how are you?

I was just working in.          
                                All good?

'''
print(multiline)

#Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

#String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good","ok"))
print(multiline)

print(len(multiline))
multiline +="                             "
multiline = "            "+multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.strip()))
print(len(multiline.strip()))

print("")

#Build a menu
title ="menu".upper()
print(title.center(20,"="))
print("Coffee".ljust(16,".") + "$1".rjust(4))
print("Muffin".ljust(16,".") + "$2".rjust(4))
print("Cheescake".ljust(16,".") + "$6".rjust(4))

print("")

#string index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some methods return boolean data
print(first.startswith("R"))
print(first.endswith("E"))


#Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue,bool))

# Numeric data type

# interger type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type (used for electrical engeniering)
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Buil-in fuctions for numbers

print(abs(gpa))
print(abs(gpa* -1))

print(round(gpa))

print(round(gpa,1))

import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))


#Casting a string ti a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data 
#zip_value = int("New York")
