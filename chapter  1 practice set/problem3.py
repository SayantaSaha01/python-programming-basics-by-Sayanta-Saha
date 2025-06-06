import os

# Direct path set karo
directory_path = "C:\\Users\\LENOVO\\OneDrive\\Documents"  # Windows
# directory_path = "/home/yourname/Documents"   # Linux/macOS

# Contents print karo
contents = os.listdir(directory_path)
for item in contents:
    print(item)





# ye code  directory path set karne ke bad jo hai usme wo show kar raha hai 