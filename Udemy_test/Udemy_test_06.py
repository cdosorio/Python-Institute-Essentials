pi = float(input()) 
radius = int(input())  # when 1.0 is entered, -> Error , invalid literal for int()
area = pi * radius **2 
print(area) 


lst = [x for x in range(3)] # list comprehension
print(lst)


ones = [1]
ones_again = ones.extend([11,111])
print(ones)
print(ones_again) # print None, because the extend() function does not return anything


def fun(a, b=1, c=4):
    print(a + b + c)
 
fun(1, 2) #  a,b positional arguments
fun(5, c = 2) # a as positional arguments, b defaulted, c as keyword arg.
fun(c = 8, a = 3) #  a,c as keyword args, b defaulted


high_fives = [10, 0, 5, 15]
high_fives.sort(reverse=True) # sorts values in descending order.
print(high_fives)


address_book = {'name': "John", 'age': 23, 'city': "London"}
 
while address_book:
    address_book.popitem() # all the items are deleted as the loop iterates 
print(address_book) # -> empty list