import os
directory = "" #directory place here
directory = directory.replace('\\', '/')
for filename in os.listdir(directory):
    if filename.endswith(".lnk"): 
        file = os.path.join(directory, filename).replace('\\', '/')
        print(file)
        os.startfile(file)
input("Press enter to exit...")