from black import out


var_a = 2
var_b = 33
print(var_a)    # outputs: 2


def return_var():
    global var_a # no crea otra variable, y afecta el valor fuera de la fn
    var_a = 5
    var_b = 44 # NO afecta el valor fuera de la fn
    print (var_b) # outputs: 44
    return var_a


print(return_var())    # outputs: 5
print(var_a)    # outputs: 5
print (var_b)  # outputs: 33


