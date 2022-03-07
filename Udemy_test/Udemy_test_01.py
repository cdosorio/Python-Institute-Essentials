print (0 ** 1)
print (3 ** 0 ** 1)
print (9** 3 ** 0 ** 1)

def default(x, y=5):
    print( y , x)
default(1)


Dict = {'Name': 'Python', 1: [1, 2, 3, 4], 2: "hi"}
print(Dict)


Tupl = ['Python', 'Tuple']
print(tuple(Tupl))


dict1 = {1:"One", 2:"Two"}
dict1[3] = "One"
print(dict1)


def sum(a,b):
  return a * b
  return a + b
print(sum(2,3))


print (5//4) # floor div


def swap(x, y): # changed only within its scope    
    z = x;
    x = y;
    y = z;    
x = 5
y = 10
swap(x, y)
print(x , y)


def put(x):
    return [6,] 
 
val = [0, 1, 2, 3, 4, 5]
y = put(val); # The returned value is stored in y , overwriting the old value
print(type(y))


milk_left = "None"
if milk_left:
    print("Groceries trip pending!")
else:
    print("Let's enjoy a bowl of cereals")


name = input()
print(name == "John") # Python is case-sensitive


weekdays = ("Monday","Tuesday","Wednesday","Thursday")
weekdays.append("Friday") # Error. Tuples are immutable
print (weekdays)


nums = [1, 2, 3, 4, 5, 6, 7]
print(nums[::-1]) # :: accesses all elements in the list but in reverse order.


full_name = "john-smith williamson"
print(full_name.title())
