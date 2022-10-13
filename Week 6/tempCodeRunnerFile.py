
firstfile = input("Enter the name of first file(must file exist) ")
f1=open(firstfile,'r')
a=sorted(f1)
for i in a:    
    print(i)
