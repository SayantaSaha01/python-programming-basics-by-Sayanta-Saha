class mother:
    def samy(self,number,company):
        self.number=number
        self.company=company
        print("hello world")
        print(f"the number is {self.number} , and company is {self.company}")
class father:
    def samuel(self,name,company):
        self.name=name
        self.company=company
        print("hello world mere vai")
        print(f"the name is {self.name} , and company is {self.company}")


class son(mother,father):
    pass

a=son()
a.samuel("rahul","IBM")
a.samy(60,"HP")

    
