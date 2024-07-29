#Program to check whether ther values inside a list are even or odd - if value is of string type, the o/p must be "invalid datatype"
list1 = [1,2,5,"string",7,4,3,11,"dk",22]

for val in list1:
    if (type(val) == int):   # if(isInstance(val,int)):
        if(val%2==0): 
            print(val, "is even")
        else:
            print(val, "is odd")
    else:
        print("Invalid data type")