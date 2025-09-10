a = ()  # firt thing to know tuples are immutable , it kind of act like list but main difference is mutability
print(type(a))  # its  a example of empty tuple

b = (1)
print(type(b)) # b = (1) is just an integer in parentheses, not a tuple.
               # Python reads it as: b = 1 → so it's an int.

c = (1,)
print(type(c))  # c = (1,) has a comma, which is what actually makes it a tuple.
                # Even if it’s one element, the comma is required to define a tuple.



t =(12,23,"65",'43','sayanta')
print(t.count(23))  #it count index value

# here focous on t and m variable program its give same result but written style are different upper styel are shorter 
#its possible in tuples and string because due to immutability its not able to change original value, but in list you dont able to do it.

m=(12,23,"65",'43','sayanta')
no=m.count(23)
print(no)

# output
# <class 'tuple'>
# <class 'int'>
# <class 'tuple'>
# 1
# 1
