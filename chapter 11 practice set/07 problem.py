# Override the __len__() method on vector of problem 5 to display the dimension of the 
# vector. 
class vector:
    def __init__(self,list):
        self.list=list

    def __len__(self):
        return len(self.list)
    
ex1 =vector([3,5,6])
print(len(ex1))

# output
# 3