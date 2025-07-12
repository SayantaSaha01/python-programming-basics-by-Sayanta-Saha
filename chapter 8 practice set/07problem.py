# Write a python function to remove a given word from a list ad strip it at the same 


l=["sayanta","rahul","priya","an"]
n=[]
def rem(l,word):
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
            
    return n
        
print(rem(l,"an"))











