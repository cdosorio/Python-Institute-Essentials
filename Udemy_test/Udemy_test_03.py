def fun(*val): 
    print(type(val)) # Arguments will be passed to the function as a tuple and printed.
 
lst=[1,2,3,4,5]
number = 400
fun(lst,number)


greeting = "Good Morning"
 
for ch in greeting:
  if ch == 'o':
    break # exit loop, including else
  print(ch)
else:
  print("Good Night")


p = 10
q = 10
print(id(p)) 
print(id(q))
print(p is q) # checks whether both the operands refer to the same object or not.


numbers = dict([('first', 3),('second', 1),('third', 2)])
print(numbers.pop('second')) #  it will fetch the value associated with the key second
#Pop: removes and returns the last value from the List or the given index value


val = ['Python', 'Tuple']
val_t = tuple(val)
val_t.pop() #  tuples are immutable, Error.
print(val_t)


greeting = "Knowledge Is Power"
print(greeting[::]) # step defaults to 1, , hence the whole string is printed


print("Hello","World", end=" ") # default sep is " "
print("Python")


nums = [1, 2, 3, 4, 5, 6, 7] # step is -5 -> list is accessed in reverse and includes every 5th element starting from the back of the list.
print(nums[::-5])