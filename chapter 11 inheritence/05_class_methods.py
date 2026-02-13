class empolyee:
    language="python"  #this is a class atribute
    @classmethod  #its use for forcefully using class method. 
    def manish(self):
        print(f"manish's favorite language is {self.language}")

a= empolyee()
a.language="java" # here ignore the instace attribute because we use @classmethod  inner clkass.
a.manish()

# output
# manish's favorite language is python