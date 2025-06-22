sayanta = {
    "character" : " gentelemn", "marks" : 78,  # you can write multiples keys in one lie usig coma,  here "character" is one example of key
    "relationship status" : "single",
    "humar": "good",
    3:8
}
print(sayanta.items())   # Prints all key-value pairs as dict_items
print(sayanta.keys())    # Prints all keys
print(sayanta.values())  # Prints all values

# Update the dictionary with new key-value pairs
sayanta.update({"humar": "best" , "looks":"handsome"})  # here update the value of humar key , and you can also add new  key like "looks"
print(sayanta)  # Prints the updated dictionary due to mutability

print(sayanta.get(3, )) # its a method to fins values of key
print(sayanta[3]) # it gives same value

print(sayanta.get("hobby")) #  why required .get method when we have normal indexing , it gives us  None because key are not exist
print(sayanta["hobby"])# it gives us KeyError , its main difference 


# output
# dict_items([('character', ' gentelemn'), ('marks', 78), ('relationship status', 'single'), ('humar', 'good'), (3, 8)])
# dict_keys(['character', 'marks', 'relationship status', 'humar', 3])
# dict_values([' gentelemn', 78, 'single', 'good', 8])
# {'character': ' gentelemn', 'marks': 78, 'relationship status': 'single', 'humar': 'best', 3: 8, 'looks': 'handsome'}
# 8
# 8
# None
# Traceback (most recent call last):
#   File "c:\Users\LENOVO\OneDrive\Desktop\python programming basics by Sayanta Saha\chapter 5\dict_methods.py", line 19, in <module>
#     print(sayanta["hobby"])# it gives us KeyError , its main difference
#           ~~~~~~~^^^^^^^^^
# KeyError: 'hobby'

