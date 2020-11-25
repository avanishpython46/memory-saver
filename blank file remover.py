import os
count = 0

def delete_files():
    global count
    for files in os.listdir():
        if files.endswith('py'):
            count+=1
            with open(files,'r') as f:
                  content = f.read()
            if len(content)==0:
                  os.remove(files)
            print(count)
              
delete_files()
