# . Create a class (2-D vector) and use it to create another class representing a 3-D 
# vector. 
class twoDvector():
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"the 2-D vector is: {self.i}i+{self.j}j")


class threeDvector(twoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
        print(f"the 3-D vector is: {self.i}i+{self.j}j+{self.k}k")

a=twoDvector(2,4)
a.show()
b=threeDvector(7,8,5)
b.show()


# output
# the 2-D vector is: 2i+4j
# the 3-D vector is: 7i+8j+5k

        
         