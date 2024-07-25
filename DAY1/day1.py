#This is for comments 

#Datatypes in python 
#1. Sequence - List, tuple, string
#2. Dictionary 
#3. Set 
#4. Numeric - int, float, complex 
#5. Boolean

a = 12                  #integer
b = 12.31131            #float
c = 1+2j                #complex

d = "String"            #string

e = True                #boolean

ls = [10, "abc", 23.32, [1,2,3]] #list
# ls[1] --> for accessing elements in the list
# Lists are mutable and indexed
# ls[0] = 15
# print(ls) 

tup = (10, "abc", 23.32, [1,2,3]) #tuple
# tup[1] --> for accessing elements in the tuple 
# Tuples are immutable and indexed
# tup[0] = 15
# print(tup[3][1])

dic = {"name": "Darshan", "age": 21, "grade": 8.3} #dictionary
# print(dic["name"])
# Dictionary is not indexed 
# Dictionary value is mutable and key is immutable  
# dic["grade"] = 9.0
# print(dic)

set = {1, 2, 3, 'abc', 90.021} #set
# set is mutable (cannot change values but can add/remove values)
# set is not indexed 

print(type(dic))         #type() is a function to get to know the datatype of the variable





