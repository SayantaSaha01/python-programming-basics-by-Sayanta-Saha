a=["sayanta","rahul",0.98,45]
a.append("koye")  #.append is built in method in list its insert the data after last index
print(a)

b =[1,4,3,2,8,9,0,7,6]
b.sort() # .short in another method  its used to short list increasing order.
print(b)

c =[1,4,3,2,8,9,0,7,6]
c.reverse() # .reverse is another method 
print(c)
print(len(c))  # len is a function its act same as string it gives us length of list

v=[1,4,3,2,8,9,0,7,6]
v.insert(2,"sayanta saha")
print(v)

i=[1,4,3,2,8,9,0,7,6]
print(i.pop(5))  #it removes the 5 index value, and its return the data which was  situated in 5 index,which is just poped
print(i) # value change now due to mutability

j=[1,4,3,2,8,9,8,7,6]
sayanta=j.pop(5)  # its same like upper , just different style
print(sayanta)
print(j) # value change now due to mutability

f=[1,4,3,2,8,9,8,7,6]
print(f.remove(9)) #its return none, means it remove the data in string which we ask
print(f) # value change now due to mutability 

# output
# ['sayanta', 'rahul', 0.98, 45, 'koye']
# [0, 1, 2, 3, 4, 6, 7, 8, 9]
# [6, 7, 0, 9, 8, 2, 3, 4, 1]
# 9
# [1, 4, 'sayanta saha', 3, 2, 8, 9, 0, 7, 6]
# 9
# [1, 4, 3, 2, 8, 0, 7, 6]
# 9
# [1, 4, 3, 2, 8, 8, 7, 6]
# None
# [1, 4, 3, 2, 8, 8, 7, 6]


