a= {1,2,3,4,5,4,"sayanta",87}
b= {1,2,3,4,5,4,"sayanta",86}
print(a.union(b)) # its gives us all value  of a  and b sets but does not repeat the value
print(a.intersection(b)) # its gives us all value which are same on both of set and b

# output
# {1, 2, 3, 4, 5, 86, 87, 'sayanta'}
# {1, 2, 3, 4, 5, 'sayanta'}