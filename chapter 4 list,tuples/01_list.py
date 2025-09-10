a=["sayanta","rahul",0.98,45]
print(a[0:2])
a[0]=87
a[1]=45
print(a[0:2])  #key different fetaure from string is lists are mutable,but indexing syntax majorthing remain same in string.a
print(a) #in list if you want to see whole result  after updation you need to print original variable , beacuse now value is change.

# output
# ['sayanta', 'rahul']
# [87, 45]
# [87, 45, 0.98, 45]

