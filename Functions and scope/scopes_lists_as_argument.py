
# inmutable: solo afectados dentro de la funcion.
# If they are mutable types (list, set, dict, etc), 
#   then you could modify them in-place inside (excepto reasignarlo completamente)


# if the argument is a list,
# then changing the value of the corresponding parameter (reassign) doesn't affect the list
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)

my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)


# but if you change a list (del, append) identified by the parameter (note: the list, not the parameter!), 
# the list will reflect the change.
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)

my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)





