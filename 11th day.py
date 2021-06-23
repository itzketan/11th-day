# 1.	Create a python module with list and import the module in another
# .py file and change the value in list
import Hello
Hello.my_function()
print("Original List")
print("------------------------------------------------")
# 3.	Import a module that picks random number and
# write a program to fetch a random number from 1 to  100 on every run
import random as r
print(r.randint(0,100))
print("------------------------------------------------")
# 4.	Import sys package and find the python path
import sys
sys.path
print(sys.path)