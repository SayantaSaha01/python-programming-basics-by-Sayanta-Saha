a =set()  #dont use a={} , because its create empty dictioary not empty set

b={1,3,4,}
print(type(b))

c={1,3,4,5,6,2,3,1,5}
print(c)  # its does not repeat dublicate value, its main usecase of set
print(type(c))

# output
# <class 'set'>
# {1, 2, 3, 4, 5, 6}
# <class 'set'>