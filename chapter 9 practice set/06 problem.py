# Write a program to mine a log file and find out whether it contains ‘python’. 



with open("chapter 9 practice set/log.txt") as f:
    content =f.read()
if ("python" in content):
    print("yes python is present")
else:
    print("pyhon is not present")
   

