#Type casting -- conversion of one datatype to another
#2 types of type casting -- 1. Implicit  2. Explicit 

#Implicit type conversion example 
a = 10
b = 22.34

sum =  a+b #Implicit type casting

print(sum) # sum is of type float


#Explicit type conversion example 
c = 2024
s = str(c)    #integer to string 
f = float(c)  #integer to float 
d = int(f)    #float to integer

print("Datatype of c", type(c))
print("Datatype of s", type(s))
print("Datatype of f", type(f))
print("Datatype of d", type(d))


#Operations --> Specific functions performed on operands using operators
#Types of operations:
#1. Arithmetic  2. Logical  3. Comparision 4. Assignement 5. Bitwise 

# 1. Arithmetic Operations 
print("Sum:", 10+20) #sum 
print("Difference:", 10-20) #difference
print("Product:", 10*5)  #multiplication 
print("Division:", 9/2)  #division --> gives you the quotient  
print("Modulo:", 10%2)  #modulo --> gives you the remainder
print("Power:", 10**2) #exponential
print("Floor Division:", 9//2) #floor division --> gives you the quotient in integer form

# 2. Logical Operations 

print("AND:", 10>5 and 20<10) #AND operator
print("OR:", 10>5 or 20<10) #OR operator
print("NOT:", not 10>5) #NOT operator

# 3. Comparision operations
print("Greater than: ", 10>5)
print("Lesser than: ", 10<5)
print("Greater than or equal to: ", 10>=10)
print("Lesser than or equal to:", 10<=23)
print("Equal to: ", 10==20)
print("Not equal to: ", 10!=20)

# 4. Assignment operations
name = "dk"

# 5. Bitwise Operation

x = 10  # Binary: 1010
y = 5   # Binary: 0101

# Bitwise AND
print(x & y)  # Output: 0 (Binary: 0000)

# Bitwise OR
print(x | y)  # Output: 15 (Binary: 1111)

# Bitwise XOR  
print(x ^ y)  # Output: 15 (Binary: 1111)

# Bitwise NOT
print(~x)  # Output: -11 (Binary: 11110101, two's complement)   ---> doubt 

# Left shift
print(x << 1)  # Output: 20 (Binary: 10100) --> doubt 

# Right shift
print(x >> 1)  # Output: 5 (Binary: 0101)  --> doubt

# Shorthand operators
x += 10   #equivalent to  x = x+10
x -= 5    #equivalent to  x = x-5
x *= 2    #equivalent to  x = x*2
x /= 3    #equivalent to  x = x/3
x %= 5    #equivalent to  x = x%5
x //= 2   #equivalent to  x = x//2
x **= 3   #equivalent to  x = x**3
print(x)


## Conditional statements 

# 1. If statement:
if 10>5:
    print("10 is greater than 5")

# 2. If-else statement:
if 10>5:
    print("10 is greater than 5")
else:
    print("10 is lesser than 5")

# 3. If-elif-else statement:
if 10>5:
    print("10 is greater than 5")
elif 10<5:
    print("10 is lesser than 5")
else:
    print("10 is equal to 5")

# 4. Switch statement:
a = 2
match a:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Something else")


## Looping Statement:

# 1. For loop:
# for(int i=1; i<10; i++)
print("For loop values -->")
for i in range(5):    
    print(i)

print("Another way of using for -->")
list1 = [1,2,3,4,5]
for val in list1:
    print(val)

for i in range(2,5):
    print(i)

print("Outside the for loop")






