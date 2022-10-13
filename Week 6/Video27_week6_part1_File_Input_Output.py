'''              File  Handling              '''

  
#  FILE INPUT AND OUTPUT
 # program to read the cntents of an existing file
 # 

file_obj = open('message','r') # Opening the file in read mode
lines = file_obj.readlines()  # reading all the lines of the file in a list called line

for line in lines: # Iterate through the list of line s fromm file
    print(line,end=' ')




# Write some message into a file called my_new_file.txt

print('Witeing to file')
f=open('My-new-file.txt','w')

f.write('Helloe This is Abhishek Kumar.\n')
f.write('Hii, This is my friend dost.. ')
f.write('Hii, This is Python with Hello world')
f.write('\n it is coll ... Hello world')
f=open('My-new-file.txt','r')
lines=f.readlines()
for line in lines:
    print(line)
f.close()


# Using file and with statement
with open('My-new-file.txt','r') as f :
    lines = f.readlines()
    for line in lines:

        print(lines,end='                  <---:--->                      ')
# f.close()
# File attributes

# FIle_Object.closed
print('\nThe file my -new -file is closed pr not ? : ',f.closed)
print('The file my-new-file is in which modes : ',f.mode )
print('The file associated with the object f is ', f.name)

f.close()