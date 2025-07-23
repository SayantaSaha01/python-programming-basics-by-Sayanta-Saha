class empolyee:
    language="python"  #this is a class atribute
    age=20

sayanta=empolyee()  
sayanta.name="sayanta saha"  #this is a instance  atribute
sayanta.language="java"  # here it prints java because inheritance attribute have higher priority than clas attribute.  
print(f"sayanta's age is {sayanta.age},sayanta's name is {sayanta.name} , sayanta's language is {sayanta.language}")

rahul=empolyee() 
rahul.name ="rahul" 
print(f"rahul's age is {rahul.age} ,rahul's name is {rahul.name}, rahul's language is {rahul.language}")