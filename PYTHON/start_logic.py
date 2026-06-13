
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

#syntax of list comprehension:
# newlist = [expression for item in iterable if condition == True]

'''the condition in the comprehension is opcional: 
With no if statement:
newlist = [x for x in fruits]'''

#in range 
newlist = [x for x in range(10)]
print(newlist)

#ex
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

#sorting lists 
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) #DESCENDING 

thislist = [100, 50, 65, 82, 23]
thislist.sort() 
print(thislist) #ASCENDING

#argument key = function.
def myfunc(n):

  return abs(n - 50) #abs = absolute value, módulo
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

"""
Para o 50: abs(50 - 50) = abs(0) = 0

Para o 65: abs(65 - 50) = abs(15) = 15

Para o 23: abs(23 - 50) = abs(-27) = 27

Para o 82: abs(82 - 50) = abs(32) = 32

Para o 100: abs(100 - 50) = abs(50) = 50

"""

#CASE SENSITIVE SORTING
#Case sensitive sorting can give an unexpected result:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#results: ['Kiwi', 'Orange', 'banana', 'cherry']
#Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower) #here
print(thislist)

#reversing the list with the method reverse()
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# THE copy() method for copying lists 
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#or the list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#or the slice operator 
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#now JOINING LISTS  
    # with + operator 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

    #with append()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

    #or with extends 
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

"""
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list

"""

#tuples  ()
mytuple = ("apple", "banana", "cherry") 
#A tuple is a collection which is ordered and unchangeable.
    #Tuples are written with round brackets ()

#in One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#tuple constructer 
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#acessing tuple's itens by index 
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#updating tuples
"""Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created."""
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#unpacking tuples: assigning the values to variables 
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#the asterisk * (list)
#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red ) = fruits

print(green)
print(yellow)
print(red) #the list is created with * 

# joining tuples with the + operator 
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#python sets {}
myset = {"apple", "banana", "cherry"}
"""
A set is a collection which is unordered, unchangeable*, and unindexed. setts are the weirdos 
Sets are written with curly brackets {}
Duplicates Not Allowed: Sets cannot have two items with the same value.
"""

#The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#accessing items 
    #You cannot access items in a set by referring to an index or a key.

    #for 
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

  #in 
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#adding new itens  add()
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#adding sets to the sets update()
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset) #but it can also be others arrays 
#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

#removing itens
#To remove an item in a set, use the remove(), or the discard() method.
thisset.discard("cherry")
thisset.remove("banana")

#You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
    #The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

    #The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

    #JOINING SETS 
"""
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() (&)  method keeps ONLY the duplicates.

The difference() (-) method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() (^) method keeps all items EXCEPT the duplicates.
"""

#The union() method returns a new set with all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#ooor you can use the | operator instead of the union() method, and you will get the same result.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2 #union here
print(set3)

#Joinin Multiple Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4) #or myset = set1 | set2 | set3 |set4
print(myset)

"""The union() method allows you to join a set with other data types, like lists or tuples.

The result will be a set. (the pipe | is used only for sets)"""

#intersection & 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2) # OR set1 & set2
print(set3)
#You can use the & operator instead of the intersection() method, and you will get the same result.

#same for differnce: 
#You can use the - operator instead of the difference() method, and you will get the same result.
#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

#FROZENSET 
"""
frozenset is an immutable version of a set.

Like sets, it contains unique, unordered, unchangeable elements.

Unlike sets, elements cannot be added or removed from a frozenset.

"""

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

#Python Dictionaries: are like javascript objects 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
"""
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

"""

#dictionary items are presented in key:value pairs, and can be referred to by using the key name.
print(thisdict["brand"])

#The dict() Constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Accessing Items
    #You can access the items of a dictionary by referring to its key name, 
    # inside square brackets:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
#There is also a method called get() that will give you the same result:
x = thisdict.get("model")

#getting the keys 
x = thisdict.keys()
#getting the values 
x = thisdict.values()

"""
Get Items
The items() method will return each item in a dictionary, as tuples in a list.
"""
x = thisdict.items() #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

#Change Values
    #You can change the value of a specific item by referring to its key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#or with the update() method, with the argument being an object with the KEY:VALUE pair
thisdict.update({"year": 2020})

#ADDING itens
thisdict["color"] = "red"
print(thisdict) #or with the update() method
thisdict.update({"color": "red"})

#REMOVING itens 
    #There are several methods to remove items from a dictionary:   

"""
The pop() method removes the item with the specified key name
The popitem() method removes the last inserted item
The del keyword removes the item with the specified key name:
    The del keyword can also delete the dictionary completely:
The clear() method empties the dictionary
"""

#LOOPING thru a dictionary 
    #printing the keys 
for x in thisdict:
  print(x)

  #printing the values 
for x in thisdict:
  print(thisdict[x]) #makes sense heheh

# or using the values() and keys() method 
for x in thisdict.values():
  print(x)

for x in thisdict.keys():
  print(x)

#Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y)

#COPYING DICTIONARYS 
    #the copy() method:
mydict = thisdict.copy()

    #with the dict() function:
mydict = dict(thisdict)

"""
Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.
"""
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#or you can also 

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#ADDING A NESTED DICTIONARY INTO A DICTIONARY
#main_dict['details'] = details_dict

#accesing itens 
print(myfamily["child2"]["name"])
#looping int nested dictionarys 
for x, obj in myfamily.items():
  print(x) #printing the values

  for y in obj:
    print(y + ':', obj[y]) #printing the values of the values 

"""
Method	Description
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary

"""


#finally, IF STATEMENTS
    #if 
a = 33
b = 200
if b > a:
  print("b is greater than a")
    #the WEIRDO python if else called elif kkk
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

    #the python switch case called match-case
    
month_number = 3

match month_number:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case _: 
        print("Invalid month")
"""
No "break" needed: Unlike in C++ or Java, Python automatically stops after it finds a match. It won't "fall through" to the next one.
The Wildcard (_): That little underscore at the bottom is your safety net. If the number isn't 1, 2, or 3, it will always trigger the "Invalid month" message.
"""
    #the ELSE statement 
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#The else statement is executed when the if condition (and any elif conditions) evaluate to False.

#One-line if/else that prints a value: PYTHON THINGY
a = 2
b = 330
print("A") if a > b else print("B")
#assigining values
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)
#syntax: variable = value_if_true if condition else value_if_false

"""
Arquivo/Módulo	snake_case	  start_logic.py
Classe	        PascalCase	  class StartLogic:
Função/Método	  snake_case	  def start_logic():
Variável	      snake_case	  my_variable
Constante	      UPPER_CASE  	MAX_SIZE
"""


#Nested If Statements
#You can have if statements inside if statements. This is called nested if statements.
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#The pass Statement
#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
  pass

#PYTHON LOOPS
  #while
i = 1
while i < 6:
  print(i)
  i += 1
  #The break Statement
  #With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#The continue Statement
#With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i) # Note that number 3 is missing in the result

#The else Statement
#With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

  #LOOPS
  #A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
  #Else in For Loop and range()
  #The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#BUUUT:
for x in range(6):
  if x == 3: break #If the loop breaks, the else block is not executed.
  print(x)
else:
  print("Finally finished!") 

  #Nested Loops
  #A nested loop is a loop inside a loop.
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#YYAAYY python FUNCTIONSSS letsagooo 
"""
Python Functions
A function is a block of code which only runs when it is called.

A function can return data as a result.

A function helps avoiding code repetition.

"""

#Creating a Function
#In Python, a function is defined using the def keyword, followed by a function name IN SNAKE_CASE and parentheses:
def my_function():
  print("Hello from a function")

my_function()

# the return statement:
def get_greeting():
  return "Hello from a function" #return a value that must be stored in a variable

message = get_greeting()
print(message)

  #argumentos e parametros 
def calcular_area_triangulo(base, altura): #parametros
    area = (base * altura) / 2
    return area

area1 = calcular_area_triangulo(10, 5) #argumentos
area2 = calcular_area_triangulo(8, 12)
area3 = calcular_area_triangulo(6, 4)

print(f"Área 1: {area1}")    
print(f"Área 2: {area2}")    
print(f"Área 3: {area3}") 

"""
A parameter is the variable listed inside the parentheses in the function definition.

An argument is the actual value that is sent to the function when it is called.
"""

#Default Parameter Values
#You can assign default values to parameters. If the function is called without an argument, it uses the default value:
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()

#Keyword Arguments
#You can send arguments with the 'key = value' syntax.
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Frani <3") #the order of the arguments does not matter.
my_function(name = "Frani <3", animal = "dog")
#When you call a function with arguments without using keywords, they are called positional arguments.
#and then the order matterssss
my_function("dog", "Frani <3")

"""The phrase Keyword Arguments is often shortened to kwargs in Python documentation."""

#Passing Different Data Types as the arguments
  #You can send any data type as an argument to a function (string, number, list, dictionary, etc.).

#sending a list
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)
#Sending a dictionary as an argument:

def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)

#To specify positional-only arguments, add , / after the arguments:
#To specify that a function can have only keyword arguments, add *, before the arguments:

"""
Combining Positional-Only and Keyword-Only
You can combine both argument types in the same function.

Arguments before / are positional-only, and arguments after * are keyword-only:
"""
  #arguments
"""
Arbitrary Arguments - *args
If you do not know how many arguments will be passed into your function, add a * before the parameter name.

This way, the function will receive a tuple of arguments and can access the items accordingly:
"""
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#What is *args?
#The *args parameter allows a function to accept any number of positional arguments.

#Inside the function, args becomes a tuple containing all the passed arguments:
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

#combining parameters
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

"""
What is **kwargs?
The **kwargs parameter allows a function to accept any number of keyword arguments.

Inside the function, kwargs becomes a dictionary containing all the keyword arguments:
"""

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

"""
Combining *args and **kwargs
You can use both *args and **kwargs in the same function.

The order must be:

  1. regular parameters
  2. *args
  3. **kwargs

"""

#we can also unpack this arguments with * for lists and ** for dicionaries 
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

#or
def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")
#what a piece of cake!!

#somethings about scope: 
  #The global keyword makes the variable global.
def myfunc():
  global x #super util!
  x = 300

myfunc()

print(x)

"""
Nonlocal Keyword
The nonlocal keyword is used to work with variables inside nested functions.

The nonlocal keyword makes the variable belong to the outer function.
"""
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x #here it is
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

"""
The LEGB Rule
Python follows the LEGB rule when looking up variable names, and searches for them in this order:

Local - Inside the current function
Enclosing - Inside enclosing functions (from inner to outer)
Global - At the top level of the module
Built-in - In Python's built-in namespace

understand:
"""
x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)
#kay??

#Python Decorators
  #A decorator is a function that takes another function as input and returns a new function.
#Define the decorator first, then apply it with @decorator_name above the function.

def changecase(func): #the func is where the function is
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction(): #also wrapper function
  return "Hello Sally"

print(myfunction())

"""
By placing @changecase directly above the function definition, the function myfunction is being "decorated" with the changecase function.

The function changecase is the decorator.

The function myfunction is the function that gets decorated.
"""

"""
Sometimes the DECORATOR function has no control over the arguments 
passed from DECORATED function, to solve this problem, 
add (*args, **kwargs) to the wrapper function, 
this way the wrapper function can accept any number, 
and any type of arguments, and pass them to the decorated function.
"""
def changecase(func):
  def myinner(*args, **kwargs): #adding to the wrapper function
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

#arguments on the decorated function
#A decorator factory that takes an argument and transforms the casing based on the argument value.
def changecase(n): #creating the parameter
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1) #adding the argument
def myfunction():
  return "Hello Linus"

print(myfunction())

"""
Lambda Functions
A lambda function is a small anonymous function. 
anonima pq nao tem nome de batismo

A lambda function can take any number of arguments, but can only have one expression.
"""

#SYNTAX: lambda arguments : expression
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6)) #can take any number of arguments

#The power of lambda is better shown when you use them as an anonymous function inside another function.
def myfunc(n):
  return lambda a : a * n

#duplicating
mydoubler = myfunc(2)
print(mydoubler(11))

#triplicating
mytripler = myfunc(3)
print(mytripler(11))

#Lambda with Built-in Functions
"""map(), filter(), and sorted()."""

  #The map() function applies a function to every item in an iterable:
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

  #The filter() function creates a list of items for which a function returns True
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#The sorted() function can use a lambda as a key for custom sorting:
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

"""
Recursion
Recursion is when a function calls itself.

Recursion is a common mathematical and programming concept. 
It means that a function calls itself. 
This has the benefit of meaning that you can loop through data to reach a result.


The developer should be very careful with recursion as it can be quite easy
 to slip into writing a function which never terminates, 
 or one that uses excess amounts of memory or processor power.
   However, when written correctly recursion can be a very efficient 
   and mathematically-elegant approach to programming.
"""
def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)#recursividade

countdown(5)

#Base Case and Recursive Case
#Every recursive function must have two parts:

#A base case - A condition that stops the recursion
#A recursive case - The function calling itself with a modified argument
#Without a base case, the function would call itself forever, causing a stack overflow error.

def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))

###################################
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))

"""
return (A função normal): Devolve o valor e mata a função. 
Ela fecha as portas, limpa a memória e tchau.

yield (O Generator): Devolve o valor e pausa a função.
 Ela fica congelada no tempo, lembrando o valor de todas as variáveis.
 Quando você chama de novo, ela acorda exatamente de onde parou.
"""

#Generators
"""
The yield Keyword
The yield keyword is what makes a function a generator.

When yield is encountered, the function's state is saved, and the value is returned. 
The next time the generator is called, it continues from where it left off.
"""

def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)

#Unlike return, which terminates the function, yield pauses it and can be called multiple times.

#next() with Generators
#You can manually iterate through a generator using the next() function:
def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

################
def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
  print(next(gen))
######################

#THE range() statement
  #syntax: range(start, stop, step)

"""
If the range function is called with only one argument, the argument represents the stop value.

The start argument is optional, and if not provided, it defaults to 0.
"""  
#range(10) returns a sequence of each number from 0 to 9. (The start argument, 
# 0 is inclusive, and the stop argument, 10 is exclusive).

print(list(range(5))) #STOPS AT 5, STARTING AT 0
print(list(range(1, 6))) #STARTS AT 1, ENDING AT 6
print(list(range(5, 20, 3))) #STARTS AT 5, GOIN TO 20 ON 3 AND 3 STEPS

#PYTHON ARRAYS:Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

#PYTHON: TRATAMENTO DE ERROS, Try Except
"""
 The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks
 """

#Exception Handling
#When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

#These exceptions can be handled using the try statement:
try:
  print(x)
except:
  print("An exception occurred")
#Since the try block raises an error, the except block will be executed.
#Without the try block, the program will crash and raise an error:

try:
  print(x)
except NameError: #will try to get the error and translate for what the dev wants
  print("Variable x is not defined")
except:
  print("Something else went wrong")

"""
ArithmeticError	            Raised when an error occurs in numeric calculations
AssertionError	            Raised when an assert statement fails
AttributeError	            Raised when attribute reference or assignment fails
Exception	                  Base class for all exceptions
EOFError	                  Raised when the input() method hits an "end of file" condition (EOF)
FloatingPointError	        Raised when a floating point calculation fails
GeneratorExit	              Raised when a generator is closed (with the close() method)
ImportError	                Raised when an imported module does not exist
IndentationError	          Raised when indentation is not correct
IndexError	                Raised when an index of a sequence does not exist
KeyError	                  Raised when a key does not exist in a dictionary
KeyboardInterrupt	          Raised when the user presses Ctrl+c, Ctrl+z or Delete
LookupError	                Raised when errors raised cant be found
MemoryError	                Raised when a program runs out of memory
NameError	                  Raised when a variable does not exist
NotImplementedError 	      Raised when an abstract method requires an inherited class to override the method
OSError	                    Raised when a system related operation causes an error
OverflowError	              Raised when the result of a numeric calculation is too large
ReferenceError	            Raised when a weak reference object does not exist
RuntimeError	              Raised when an error occurs that do not belong to any specific exceptions
StopIteration	              Raised when the next() method of an iterator has no further values
SyntaxError	                Raised when a syntax error occurs
TabError	                  Raised when indentation consists of tabs or spaces
SystemError	                Raised when a system error occurs
SystemExit	                Raised when the sys.exit() function is called
TypeError	                  Raised when two different types are combined
UnboundLocalError	          Raised when a local variable is referenced before assignment
UnicodeError	              Raised when a unicode problem occurs
UnicodeEncodeError	        Raised when a unicode encoding problem occurs
UnicodeDecodeError	        Raised when a unicode decoding problem occurs
UnicodeTranslateError	      Raised when a unicode translation problem occurs
ValueError	                Raised when there is a wrong value in a specified data type
ZeroDivisionError	          Raised when the second operator in a division is zero
"""

#Else: to define a block of code to be executed if no errors were raised
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#Finally: if specified, will be executed regardless if the try block raises an error or not.
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

  #ex
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

#Raise an exception
  #To throw (or raise) an exception, use the raise keyword.
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")

x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")

#F-Strings
  #F-string allows you to format selected parts of a string.
txt = f"The price is 49 dollars"
print(txt)

#Placeholders and Modifiers
  #To format values in an f-string, add placeholders {}, 
  # a placeholder can contain 
  #variables, operations, functions, and modifiers to format the value.

price = 59
txt = f"The price is {price} dollars"
print(txt)
#A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
txt = f"The price is {price:.2f} dollars" #modifier
print(txt)

#perfoming operations
txt = f"The price is {20 * 59} dollars"
print(txt)

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

#performing if and elses 
price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)

#executing functions 
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

#it doesnt have to be a built in method, can be a created function
def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

#the format() method 
price = 49
txt = "The price is {} dollars"
print(txt.format(price))


#ITSS ENDEDDD paraboins 





