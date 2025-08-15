class empolyee:
    language="python"  #this is a class atribute
    @classmethod  #its use for forcefully using class method.
    def manish(cls):
        print(f"manish's favorite language is {cls.language}")
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")
        self.lname=value.split(" ")

a= empolyee()
a.name="masish singh"
print(f"the name is {a.fname} {a.lname}")
print(a.name)
a.language="java"
a.manish()


# output
# the name is masish singh
# masish singh
# manish's favorite language is python