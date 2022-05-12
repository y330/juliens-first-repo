# filename: curriculum.py
# author(s): Yonah Aviv
# date modified: 05/04/2022
# date created: 05/04/2022
# status: IN PROGRESS

"""Important Words/Phrases"""
"""
run a program: start operating a file of code
compiler: computer program that interprets your coding language and converts it to a format that the computer understands (i.e. 0s and 1s). important for running programs
terminal: window that contains the information your code outputs when it runs. also able to receive user input
IDE(integated development environment): app that you can use to manage your coding projects, and write code and run it.
>> or -->: means outputs
ADVANCED: **look at this later**
GIT: tool to sync your local coding project to a git repository. good for team work because multiple people can sync the same project to their computers and edit it at the same time.
  git repository: A Git repository tracks and saves the history of all changes made to the files in a Git project.
  git commit: save progress locally
  git push: upload progress to the cloud
  git pull: import changes made to the cloud repository to your local computer.
 """"

"""Lesson 1: Printing and Code Comments"""
# this is a  code comment
# comments are used to explain code to make it more easily readable.
# comments are created by typing "#" and following it with your comment.
print("Hello")  # print some information




"""Lesson 2: Variables And Strings"""
greeting = "Hello World"
print(message)

string_with_newline = "hello, \n my name is Yonah" # use \n to denote a new line in your string
print(string_with_newline)
# reminder: to output information to the console: type print, followed by brackets enclosing the text you want to print.
# remember: surround the text with quotes, otherwise it will think you want to print an undefined variables

# TASK: in the space below, change code that will output a letter addressed to Mr. O so that it only has one variable 
      
      ####should output something like this:
      # Dear Mr. O,
      #  
      # Nice to meet you to!
      #
      # Regards,
      # Yonah
      # basically your task is to make the code below significantly shorter.
# YOUR CODE:-----
line_1 = "Dear Mr. O,"
line_2 = ""
line_3 = "Nice to meet you to!"
line_4 = ""
line_5 = "Regards,"
line_6 = "Yonah"
print(line_1)
print(line_2)
print(line_3)
print(line_4)
print(line_5)
print(line_6)
  
#---------------



"""Lesson 3: Different Types of Information"""
### In the real world, there are many different types of information, such as numbers, text, etc. In coding, there are similar types.
# these types vary depending on the language, but almost always include the following:
# 1. text: String 
# 2. number: Integer
# 3. number: Float
# 4. other: Boolean/Conditional statements

string_ = "Hello World"  # store text information of type String (a string must be any text enclosed by quotation marks) ex: "string"
# Task 3a: ouput a different string
integer_ = 3  # store number information of type Integer (an integer must be any whole number between -infinity and +infinity) ex: 300 and -2244 are both integers
# Task 3b: output a different integer
float_ = 3.4 # store number information of type Float (How is this type different from an Integer i.e., 3 vs 3.4? Answer: ______)
# task 3c output a different float
boolean_ = True # store a True/False evaluation. see more on this in the next lesson




"""Lesson 4: Comparing Information: Booleans"""
a = 1
b = 2
### Comparisions------------
### The following symbols can  be used to compare integers and floats: ==, <, <=, >, >=
                                 # Guess what these lines each will output, based on the variable names?
a_equalTo_b            = a == b  # _____
a_isLessThan_b         = a < b   # _____
a_isLessOrEqualTo_b    = a <= b  # _____
a_isGreaterThan_b      = a > b   # _____
a_isGreaterOrEqualTo_b = a >= b  # _____
## DO not run the following before you fill in the blanks 
print(f"a == b is {a_equalTo_b} \n")


"""Lesson 5: Math: Evaluating Expressions"""
expression = 4 + 2 # 4 + 2 is an expression
# * means multiplication
# + means addition
# - means subtraction
# / means division
# a ** 2 means raise variable a to the power of 2
### Predict what each expression will output before running
print(6 * 2)  # --> 
print(45 + 2 + 21)  # -->
print(6 - 13 - 23)  # -->
print(6 / 2 + 4 - 12)  # -->
print(6 ** 2) # -->

# you can only do operations on numbers, not strings. you can do addition on strings tho.
# you can make the math more complicated as well, with variables
exoression
a = 40
harder_expression = 240 / 2 - (a * 2)





"""Lesson 6: User Input"""
### you can use the terminal as a text box in python. this can be used to make interactive programs.
name = input("What is your name?")  # shows a prompt in the terminal where you can type in a string. 
                                    # even if you type in a number, it will still be a string. 
                                    # example: typing in 4 will give you "4"
                                    # to convert a variable equal to "554" into an integer 554 you type in: int(variable)
greeting = "Hello" + name  #  guess what string greeting now holds?
print(greeting)  #  print the concatonated string.



# ******************************************************************************************************************************888888
## CHALLENGE: create a program that asks the user for 4 marks out of 100 and then calculate the avaerage:

# 1. create 4 variables that ask the user to input a int mark out of 100 (ex. 67)
# 2. create another variable that hold the calculations for finding the average of the 4 marks
# hint: to calculate average, add all items, and divide by number of items
# final step: print it in a full sentence using an f-string

mark1 = input("Enter the first mark")



