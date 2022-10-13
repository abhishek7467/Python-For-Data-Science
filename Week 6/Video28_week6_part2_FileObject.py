
# Random File Access 
f=open('text.txt','w')
f.write('\nabcdefghijklmnopqrstuvwxyz')
f.write('\n Hello World\n')
f.seek(10,0)
f.write(' Hii ,This is Abhishek  ')

f.seek(6,0)
f.write('Bye')
f.seek(2,0)
f.write('PYTHON')
f.close()
with open ('text.txt','r') as f:
    for line in f:
        print(line,end=' ')

f.close()




#Serialization 
import json

f=open('student_data','w')
student=('Abhishek',23,99.9,'Bareilly')
json.dump(student, f)
# student=('Kumar',20,90.9,'Lucknow')
# json.dump(student, f)
f.close()


# Deserialization 
import json 
f= open('student_data','r')
student=json.load(f)
print('The data read is  : ', student, end=" ")
print('The type of student object is :  ', type(student))
f.close()



import os 
print ('The curent working directory is os.getcwd()  :  ',os.getcwd())
print("List the contents  of the current directory : ",os.listdir())
print('Let us create a directory calledmydir.......')
os.mkdir('mydir')
print('The contents  of the current directory are : ', os.listdir())


import os

print('-----------------')
print('Change the directory to mydir ....  ')
os.chdir('mydir')
print('The current irectory now is  : ',os.getcwd())

print('Change back to the parent directory ... ',)
os.chdir('..')
print('The current working directory now is  : ', os.getcwd())








import os  
print('The content of this directory are : ')
print(os.listdir())
print('Remove the directory mydir.... ')
os.rmdir('mydir')
print('After deleting mydir, the contents of the directory are:  ')
print(os.listdir())



