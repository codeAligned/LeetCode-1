import os

for filename in os.listdir("./"):
    if filename.endswith(".cpp"):
        f = open(filename, "r+")
        text = f.read()
        s = '// ' + filename[0:-4] + '\n' + text + '\n'
        f.close()
        f2 = open(filename, "w+")
        f2.write(s)
        f2.close()

