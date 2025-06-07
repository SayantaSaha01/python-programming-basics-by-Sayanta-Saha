# 2. Write a program to fill in a letter template given below with name and date. 
# letter = '''  
# Dear <|Name|>, 
# You are selected! 
# <|Date|> 
# '''

letter ='''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
'''
print(letter.replace("<|Name|>","sayanta") .replace("<|Date|>","28th april 2005"))  # here.replace is string built in functin by python 
# its help us to replace data in string

# ex-2

a ='''  
sir 
    Name, 
    You are hired as amanager in the name of company '''
print(a.replace(" Name","sayanta").replace ("the name of company","google"))

# output

# Dear sayanta,
# You are selected!
# 28th april 2005


# sir
#    sayanta,
#     You are hired as amanager in google