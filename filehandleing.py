f=open("D:\\file.txt","w")
f.write("THIS IS FIRST PYTHON PROGRAM")
f=open("D:\\file.txt","r")
print(f.read())
f.close()
print(f.closed)
