dict1 = {"John":1234, "Fruit":"Apples"}
dict2 = {"Fruit":"Apples", "John":1234}
print(dict1 == dict2) # True, the comparison between two dictionaries is on the basis of key-value pairs having the same positions


p = 0b1100
q = 0b1101
print(bin(p | q)) # The | (OR) operator produces 0 when both bits are 0, else produces 1


a = 'python'
i = 0
while i < len(a):
  i += 1
  pass # empty loops, do nothing
print('Value of i :', i)


data = [1, 2, "apples", 3.14, True]
del data[:2] # deletes from the beginning of the list until the element at position 1 (excluding 2).
print(data)


x = 1 
if (x < 3): print("True")
else: print("False") # if contains only one line of code, the syntax is correct.


# Continue will terminate the current iteration
# Break will terminate the entire loop


def fun(x=5,y): # Syntax error, The non-default argument should be preceded by the default-argument
    return x/y
print(fun(2))


print("Hello","World",sep=None) # None behaves exactly as the default separator, which is the space.
# An empty print() statement will print a blank line. An invisible new line character (\n) will be introduced by default.


tupl1 = (-1, 0, 1)
tupl2 = ('bananas')
tupl3 = (tupl1, tupl2) # we did not use the concatenation operator. Instead, tupl1 and tupl2 were enclosed in a tuple
print(tupl3)

