class empolyee:
    language="python"  #this is a class atribute
    @classmethod  #its use for forfully using class method.
    def manish(cls):
        print(f"manish's favorite language is {cls.language}")

a= empolyee()
a.language="java"
a.manish()
