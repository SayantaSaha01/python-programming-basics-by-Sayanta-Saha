def goodday(name,ending="thanks"):  # here ending="thanks" it is work as default parameter
    print(f"good day,{name},{ending}")

goodday("sayanta","yeah") # here ignore the default parameter because  this "yeah"  works here
goodday("sayanta") # here works defaults parameter because here no extra arguments while calling function


# output
# good day,sayanta,yeah
# good day,sayanta,thanks