# FIle copy application
sourece_file = input('Enter the name of the source file :  ')
destination_file= input('Enter the name of the destination file : ')
f1=open(sourece_file,'r')
f2=open(destination_file,'w')

while True:
    data=f1.read(1)
    if data==' ':
        break

    f2.write(data)

f1.close()
f2.close()





# File append application

sourece_file=input('Enter the name of the source file : ')
Destination_file=input('Enter the name of the Destination file : ')
f1=open(sourece_file,'r')
f2=open(Destination_file,'a')

while True:
    data=f1.read(1)
    if data==' ':
        break

    f2.write(data)

f1.close()
f2.close()







