class empolyee:
    language="python"  #this is a class atribute
    @classmethod  #its use for forfully using class method.
    def manish(cls):
        print(f"manish's favorite language is {cls.language}")
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
a.language="java"
a.manish()
