class empolyee:
    def manish(self):
        print(f"manish's favorite language is {self.language}")
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

a= empolyee()
a.name="masish singh"
print(f"the name is {a.fname} {a.lname}")
print(a.name)



# output
# the name is masish singh
# masish singh
