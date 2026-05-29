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
