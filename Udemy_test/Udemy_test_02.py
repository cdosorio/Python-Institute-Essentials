def myprint(*val): # functions expects multiple arguments.
   print(val)
myprint("Peter","Piper","Pickled","Pepper")


val = 5
print("less than 10") if val < 10 else print("greater than 10")  # employed if both statements have only one line to be executed.


def fun(a = 3, b = 2): # When calling the function with one value, we are setting and using the positional argument while the value b is defaulted to 2.
    return b ** a
 
print(fun(2)) # lo asigna a variable "a"


x = 0
for i in range(10): # iterates 10 times (o to 9)
  for j in range(-1, -10, -1): # negative range, iterates 9 times
    print(j)
    x += 1
print(x)


if 1 == 1.0: # The value of the numbers are the same even they they are of different types
    print("Values are the same")
else:
    print("Values are different")


a = 0b1011 
b = 0b1001
print(0 ^ 0) # 0
print(1 ^ 0) # 1
print(1 ^ 1) # 0
print(bin(a ^ b)) # The XOR operator (^) evaluates to 1 if either of the bits are 1.


s1="Hello Mr Smith"
print(s1.capitalize()) # capitalizes the first letter of the first word (diferente a TitleCase)