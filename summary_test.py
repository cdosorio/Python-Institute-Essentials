# 1: tuples are inmutable -> illegal
tup = (1,2,3)
tup[1] = tup[1] + tup[2]
print(tup)

# 5 print # # #
lst = [[x for x in range(3)] for y in range(3)] 
print(lst)
for r in range(3): 
    for c in range(3): 
        if lst[r][c] % 2 != 0:
             print("#") 

# 8: 1,1,2
x= 1
y = 2
x,y,z = x,x,y
z,y,z = x,y,z
print(x,y,z)

# q11
nums = [1,2,3]
vals = nums
del vals[:]

# q 13
dct = {'one': 'two', 'three': 'one', 'two': 'three'} 
v = dct['three'] 
for k in range(len(dct)):
     v = dct[v] 
print(v) 

# 15
foo = (1,2,3)
foo.index(3) # index of 3

# 25
def fun(a,b, c= 0):
     return a+b+c

print(fun(b=3, a=5))

# 26 : 4
tup = (1,2,4,8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)

# 27 : break es solo para loop
try:
     print(5/0)
     break
except:
     print('Sorry, something went wrong...')
except (ZeroDivisionError):
     print('Too bad')

# 28 : zero. El primero debe ser menor
list = [i for i in range (-11, -2)]
print(len(list))

# 30
list = [0,1,4,9,16]
def fun(lst):
     del lst[list[2]] # borra el 16
     return lst

print(fun(list))

# 31: Error , positional argument follows keyword argument
def func(a,b):
     return b ** a 

print(func(b=2, 2))


# 32 : insert con indez negativo es lo mismo que index cero
list = [1,2]
for v in range(2):
     list.insert(-10, list[v])

print(list)

# 34 : precedencia: //  /  +
x = 1 // 5  + 1 / 5
print (x)