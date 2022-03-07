name, phone, location = "John", 123455667, "London" # Multiple variables can be assigned values as shown
print(name, phone, location)


area = 25.6
area = int(area) # The int function will round down
print(area)


lst1 = [2,4,6]
lst2 = [2,4,6]
 
print(lst1 is lst2) # lst1 and lst2 are two different objects -> False
print(lst1 == lst2) # checks if the values stored in the variables are equal  -> true


groceries_list1 = ["Milk", "Cheese"]
groceries_list2 = ["Bread", "Butter"]
groceries_list1.extend(groceries_list2) # adds the second list to the main list
print(groceries_list1)


for i in range(1, 3):
    print(i)
else:
    print("hi") # In a for-else loop, the else block is always executed (except with break)


i = 0
while i < 4:
    i += 1
    print(i)
    break # the break statement will terminate the loop after the first iteration (the else won't be executed)
else:
    print("Break")


def fun(x):
    x[-1] =  "c" # it does change the list provided as an argument, the change is visible outside.
    # pero si cambia la lista entera, entonces no será visible afuera
val = ["a","b","c","d"]
fun(val); # semi-colon is not mandatory. Denotes separation, rather than termination.
print(val)


def fun(**names): # **names is used to pass a keyworded, variable-length argument (name-value pairs).
    for key, value in names.items():
        print(key, value, end=" ", sep=":")
 
fun(NAME="John",AGE=29, CITY="London")