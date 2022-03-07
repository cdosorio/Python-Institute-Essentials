#  Tuples are ordered and unchangeable (immutable) collections of data.

one_element_tuple_1 = (1, )

# Loop
my_tuple = (1, 10, 100)
for elem in my_tuple:
    print(elem)

# join
t1 = my_tuple + (1000, 10000)
print(t1)

# multiply 
t2 = my_tuple * 3
print(len(t2))
print(t2)

# check existence
print(10 in my_tuple)
print(-10 not in my_tuple)

# swap values 
var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1 

print(t1, t2, t3)

# count ocurrences
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)
print(duplicates)    # outputs: 4


# tuple to list
tup = 1, 2, 3, 
my_list = list(tup)
print(type(my_list))    # outputs: <class 'list'>

# list to tuple
my_list = [2, 4, 6]
tup = tuple(my_list)
print(type(tup))    # outputs: <class 'tuple'>

# tuple to dict
colors = (("green", "#008000"), ("blue", "#0000FF"))
colors_dictionary = dict(colors)
print(colors_dictionary)


