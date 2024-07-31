#Program to find whether a value is even or odd through quotient - if its not a integer value then print "invalid value"

# Traversing through the list 

list2 = [1,2,5,"string",7,4,3,11,"dk",22]

for val in list2:
    #checking the type of the value
    if(type(val) == int):
        if (type(val/2) == int):
            print(val, "is even")
        else:
            print(val, "is odd")
    else:   
        print("invalid value")




