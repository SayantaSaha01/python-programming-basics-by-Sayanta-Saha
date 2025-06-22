# Tuple Creation
t = (1, 2, 3, 2, 4, 5)

# count() → Count occurrences of a value
print(t.count(2))       # Output: 2

# index() → First index of a value
print(t.index(3))       # Output: 2

# Indexing
print(t[0])             # Output: 1

# Slicing
print(t[1:4])           # Output: (2, 3, 2)

# Length
print(len(t))           # Output: 6

# Membership check
print(4 in t)           # Output: True
print(10 in t)          # Output: False

# Concatenation
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)          # Output: (1, 2, 3, 4)

# Repetition
print(t1 * 3)           # Output: (1, 2, 1, 2, 1, 2)

# Iteration
for item in t:
    print(item)

# Tuple Unpacking
a, b, c, d, e, f = t
print(a, b, c)          # Output: 1 2 3

# Nested Tuple
nested = (1, (2, 3), (4, 5))
print(nested[1][0])     # Output: 2

# Conversion: List to Tuple
lst = [10, 20, 30]
a = tuple(lst)
print(a)    # Output: (10, 20, 30)

b = [10, 20, 30]
print(tuple(b)) #its same like before just shorter

# Conversion: Tuple to List
tup = (100, 200)
c = list(tup)
print(c)    # Output: [100, 200]







