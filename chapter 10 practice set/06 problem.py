'''  Can you change the self-parameter inside a class to something else (say 
 “harry”). Try changing self to “slf” or “harry” and see the effects. '''

from random import randint
class train:

    def __init__(sel,trainno):
        sel.trainno=trainno

    def book(harry,fro,to):
        print(f" your train no: {harry.trainno} destination from {fro} to {to}")
    def getstatus(self):
        print(f" your train no: {self.trainno} is on rirgt time")
        
    def getfare(self,fro,to):
        print(f" your train no: {self.trainno} destination from {fro} to {to} and is price is: {randint(200,700)}")

kashmir= train(2316)
 
kashmir.book("kolkata","kashmir")
kashmir.getstatus()
kashmir.getfare("kolkata","kashmir")   


#ANS IS KUCH VI FARAK NAHI PADHEGA