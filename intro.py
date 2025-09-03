##python is a high level , interpreted , 
#object - oriented programming language created by 
#guido van rossum in 1991.

# it is known for its simple syntax that resembles 
# English , which makes it beginner- friendly and
#  widely used in 
# fields like web development , 
# data sci , AI  , automation , machine learning 
# and more.

#key features of python:- 

#1 -- simple and easy to understand/ learn 
#--> syntax is very clean and similar to english 
#--> makes it beginner friendly
#ex -- print("hello world")

#2 -- Interpreted language 
## --> no need for compilation 
##--> python code is executed line by line using the 
##python interpreter

##3 -- Cross - platform
# --> python code can be run on any operating system
# example - Windows , Mac , Linux
# write once , run anywhere  

#4 - Open source and free 
# --> python is a free and open source programming
# language , which means that anyone can use it for
# free and modify it to their liking.

#5 -- obejct-oriented prog
# supports classes , objects , inheritance , 
# polymorphism , encapsulation , abstraction.  

#6 ---dynamic typing
#  here you dont have to declare the data type 
# of the variable.
#python will automatically detect the data type.
# a = 10 #int 
#  a = "hello" #string

#7 -- Extensive standard library
#--> comes with a large collection of modules 
#and functions that can be used to perform 
#various tasks.
# reduces the need to write code from scratch.
#ex -- web development -- flask , django
#ex -- machine learning -- numpy , pandas , scikit-learn

#8 -- Huge community support
#--> active community with millions of developers, 
# tutorials, and resources.

#9 -- Scalable 
#--> can integrate with C , C++ , Java , and other 
#programming languages.

#10 -- Wide applications 
#--> web development - flask , django 
#--> Data sci and ai -- pandas , numpy , scikit-learn
#--> game development - pyglet , pygine, pygame
# desktop apps - tkinter , wxpython
##automation - selenium , robotframework

##in short 
# python = Simple + Powerful +versatile -->"A language 
# for everyone
# 
# 
#Variables -- 
# a container for storing data values
# 
# a variable in python is simply a name that refers to 
# a value stored in a memory location. 
# a = 10 
# a = True
# a is variable storing an integer value 10.
# a is variable storing a boolean value True.

##features of variables in python 
#1 - no need for explicit declaration
#2 - dynamic typing 
#3 - case sensitive
#4 - no need for semicolons
#5 - flexible types - int , float , string , boolean ,
#6 - memory management 
#--> python automatically handles memory allocation
#and garbage collection.

# rules for naming variables 
#1 - must start with a letter or underscore
#2 - can contain letters , numbers and underscores
# (a-z, A-Z , 0-9 , _)
# 3 - cannot start with a number
# 4 - spaces are not allowed
# 5 - variable names are case-sensitive
# 6 - reserved keywords cannot be used as variable names
#( true , if , while )

# print = 10 
# if = 10 

# 23/08/25
##Types of variables
 #1 - global variables 
 #2 - local variables
 #3   constants

#1 - global variables 
#--> variables that are defined outside of any function 
#or block are called global variables.
# they can be accessed from anywhere in the program.

#local variables --
#--> variables that are defined inside a function or block 
#are called local variables.
# they can only be accessed within that function or block.

#constants 
#--> variables that are defined with a constant value 
#cannot be changed once they are assigned.
 
# python doesnt have true constants , but we use 
# uppercase name 
# to indicate that a variable is a constant.
# ex -- PI = 3.14


##operators 
# In python , operators are symbols that perform 
# specific operations on operands/variables and values.

#1 - arithmatic operators 
#2 - assignment operators 
#3 - comparison operators 
#4 - logical operators 
#5 - identity operators 
#6 - membership operators 
#7 - bitwise operators

#1 - arithmatic operators 
# + -- addition -- add two values 
# ex --- print(x+y)
# print("py" + "thon")
# -    -- subtraction -- subtract the right operand 
# from the left operand
# ex -- print(x-y)
# *  -- multiplication -- multiply two values
# ex -- print(x*y)
#ex -- print("py" * 3)
#  / - -- division -- divide the left operand by the 
# right operand
# ex -- print(x/y)
#  % - -- modulus -- return the remainder after divison 

# // - -- floor division -- divide and returns the 
#largest whole number (integer part only)
# ** -- exponentiation -- raise the left operand to 
# the power of the right operand

#comparison op --
# > -- greater than
#true if left values is greater than right 
# < -- less than
# true if left is smaller than right 
# >= -- greater than or equal to
#true if left is greater than or equal to right
# <= -- less than or equal to
#true if left is less than or equal to right
# == -- equal to
# != -- not equal to


#3 assignment op -- used to assign values to variables 
# = -- assign value to variable
# += -- add and assign
# -= -- subtract and assign
# *= -- multiply and assign
# /= -- divide and assign
# %= -- modulus and assign
# //= -- floor division and assign
# **= -- exponentiation and assign


#4 logical op -- used to perform logical operations 
# and -- returns true if both operands are true
# or -- returns true if either operand is true
# not -- returns true if the operand is false

#5 identity op -- returns true if both operands 
# refer to the same object(whether two objects 
#are stored at same memory location or not)
# is not -- returns true if both operands do not 
# refer to the same object
# is -- returns true if both operands refer to the
#  same object

#6 membership op -- returns true if the specified 
# sequence is present in the object
# in -- returns true if a sequence with the specified 
# value is present in the object
# not in -- returns true if a sequence with the 
# specified value is not present in the object

#bitwise op 