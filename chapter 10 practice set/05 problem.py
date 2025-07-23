# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways. 
from random import randint
class train:

    def __init__(self,trainno):
        self.trainno=trainno

    def book(self,fro,to):
        print(f" your train no: {self.trainno} destination from {fro} to {to}")
    def getstatus(self):
        print(f" your train no: {self.trainno} is on rirgt time")
        
    def getfare(self,fro,to):
        print(f" your train no: {self.trainno} destination from {fro} to {to} and is price is: {randint(200,700)}")

kashmir= train(2316)
 
kashmir.book("kolkata","kashmir")
kashmir.getstatus()
kashmir.getfare("kolkata","kashmir")

