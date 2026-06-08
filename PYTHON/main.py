
print("Oiii Python 😎")
#nome = input("Nome: ")
#print("Oii", nome)

#Python can be treated in a 
# procedural way, an object-oriented way or a functional way.
#Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
#Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.

#IDENTAÇÃO
if 5>2: 
    print("Five is bigger than two!")
        #indentação eh importante no python 
#or 
if 5>2:
 print("Five is bigger than two!") #normalmente a indentação tem 4 espaço, mas pode ter quantas quiser

#VARIAVEIS 
x = 5
y = "Hello, World!"
#aaaaaaaaaaaaaaah que agoniaaagh uhauhsuhsu, sem tipagem

#In Python, a statement usually ends when the line ends. You do not need to use a semicolon (;) like in many other programming languages (for example, Java or C).

print("Hello"); print("How are you?"); print("Bye bye!") #uso de semicolunas

#printar sem linha nova 
print("Hello World!", end=" ")
print("I will print on the same line.")

"""
This is a comment
written in
more than just one line
"""

#CASTING, tipando os dados 
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x, y, z)
print(type(x))
print(type(y))
print(type(z))
#Variable names are case-sensitive.

"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
"""
a, b, c = "Orange", "Banana", "Cherry"
print(a)
print(b)
print(c)

'''Complex: Complex numbers are written with a "j" as the imaginary part:'''
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#numero randomico 
import random
print(random.randrange(1, 10))

#STRINGS
#You can assign a multiline string to a variable by using three quotes: 

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#strings are arrays 
a = "Hello, World!"
print(a[1])
print(len(a)) #len conta o numero de caracteres da string, incluindo os espaços

for x in "banana":
  print(x)


txt = "The best things in life are free!"
if "free" in txt: #in verifica 
  print("Yes, 'free' is present.")

print("expensive" not in txt) #valor booleano


#slicing 
b = "Hello, World!"
print(b[2:5]) #Slicing
print(b[:5])#Slice From the Start
print(b[2:]) #Slice To the End
print(b[-5:-2]) #Negative Indexing

#F-Strings 
"""
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
"""
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Escape Character
#An escape character is a backslash \ followed by the character you want to insert.
txt = "We are the so-called \"Vikings\" from the north."

#Python é dinâmica (o tipo muda conforme o valor) e forte (você não pode somar inteiro + string sem fazer o casting que você anotou: int("3")).

"""Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones."""

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])  # all true

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) #all false (the only)

#arithmetic operators
x = 15
y = 4

print(x + y) #soma
print(x - y) #subtração
print(x * y) #multiplicação
print(x / y) #divisão
print(x % y) #módulo
print(x ** y) #exponenciação
print(x // y) #divisão euclidiana (floor division)

#the ternary operator
num = 6

x = "WEEKEND!" if num > 5 else "Workday"

print(x)
#equals tooo

if num > 5: 
    x = "WEEKEND!" 
else:
    x = "Workday"

#logical operators 
a = 5
print(a > 3 and a < 10) #and
print(a > 3 or a < 4) #or
print(not(a > 3 and a < 10)) #not

#indenty operators
"""is 	Returns True if both variables are the same object		
is not	Returns True if both variables are not the same object"""
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

"""Difference Between is and ==             
is - Checks if both variables point to the same object in memory
== - Checks if the values of both variables are equal"""
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y) #true
print(x is y) #false


#Python Collections (Arrays)
"""There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members. []
Tuple is a collection which is ordered and unchangeable. Allows duplicate members. ()
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members. {} as javascript objects"""




#PYTHON LISTS []
#Lists are used to store multiple items in a single variable.
#Lists are created using square brackets: []
#List items are ordered, CHANGEABLE, and allow duplicate values.
mylist = ["apple", "banana", "cherry"]
print(len(mylist))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
    #acessing itenns 
print(thislist[1])
    #changing item value
thislist[1] = "blackcurrant"
print(thislist)
    #inserting items
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.
thislist.insert(2, "watermelon")
    #appending items
thislist.append("grape")
#To add an item to the end of the list, use the append() method:
    #extending a list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
    #removing items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
    #removing an item by index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) #If you do not specify the index, the pop() method removes the last item.
#The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist
    #cleaning the list 
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

    #looping through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#or thru indexes
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#USING THE WHILE LOOP
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#list comprehension
    #NO COMPREHENSION
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
    #COMPREHENSION
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x] #here

print(newlist)




