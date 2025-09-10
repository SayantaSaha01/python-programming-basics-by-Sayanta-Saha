a= {1,2,3,4,5,4,"sayanta",87}
print(a,type(a))

a.add(98)
print(a,type(a))

a.remove(1)
print(a,type(a))

a.discard(76)
print(a)  #


# output
# {1, 2, 3, 4, 5, 'sayanta', 87} <class 'set'>
# {1, 2, 3, 4, 5, 'sayanta', 87, 98} <class 'set'>
# {2, 3, 4, 5, 'sayanta', 87, 98} <class 'set'>