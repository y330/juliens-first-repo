# filename: hello_world.py
# author(s): Yonah Aviv
# date modified: 05/04/2022
# date created: 05/04/2022

"""Important Words/Phrases"""
"""
run a program: start operating a file of code
compiler: computer program that interprets your coding language and converts it to a format that the computer understands (i.e. 0s and 1s). important for running programs
terminal: window that contains the information your code outputs when it runs. also able to receive user input
IDE(integated development environment): app that you can use to manage your coding projects, and write code and run it.

ADVANCED: **look at this later**
GIT: tool to sync your local coding project to a git repository. good for team work because multiple people can sync the same project to their computers and edit it at the same time.
  git repository: A Git repository tracks and saves the history of all changes made to the files in a Git project.
  git commit: save progress locally
  git push: upload progress to the cloud
  git pull: import changes made to the cloud repository to your local computer.
 """"

"""Lesson 1: Printing and Code Comments"""
# this is a  code omment
# comments are used to explain code to make it more easily readable.
# comments are created by typing "#" and following it with your comment.
print("Hello")  # print some information




"""Lesson 2: Variables"""
greeting = "Hello World"
print(message)




"""Lesson 3: Different Types of Information"""

string = "Hello World"  # store text information of type String (str). if "4" is a string and 4 is not, what do you think makes information a string

integer = 3  # store number information of type Integer (int)

floating_pt_number = 3.0 # Floating-point Number (float). How is this type different from the type int? answer: 





"""Lesson 4: Comparing Information: Booleans"""
a = 1
b = 2
### Comparisions------------
a == b  #|#     a is equal to b                 >> False
a <= b  #|#     a is less than or equal to b    >> True
a <  b  #|#     a is less than b                >> True
a >= b  #|#     a is greater than or equal to b >> False
a >  b  #|#     a is greater than b             >> False



"""Lesson 5: Math"""
### Predict what each line will output before running
print(6 * 2)  # 6 x 2 == ?
print(6 + 2)  # 6 + 2 == ?
print(6 - 2)  # 6 - 2 == ?
print(6 / 2)  # 6 ÷ 2 == ?
print(6 ** 2) # 6²    == ?

# you can only do operations on numbers, not strings. you can do addition on strings tho.
# you can make the math more complicated as well





"""Lesson 6: User Input"""
### you can use the terminal as a text box in python. this can be used to make interactive programs.
name = input("What is your name?")  # shows a prompt in the terminal where you can type in a string. 
                                    # even if you type in a number, it will still be a string. 
                                    # example: typing in 4 will give you "4"
                                    # 
greeting = "Hello" + name  #  guess what information is now in the variable greeting?
print(greeting)  #  print the concatonated string.

#Task: create a program that asks the user for 



