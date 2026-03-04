'''file=open('sample.txt','r')

content1=file.read()
file.seek(0)
content2=file.readline()
file.seek(0)
content3=file.readlines()
print(content1,content2,content3,sep='\n\n')
file.close()'''

'''file=open('samples.txt','w')
file.write("Hello Everyone")
file.close()'''

'''file=open('sample.txt','a')
file.write("\nWelcome to the Python class")
file.close()'''


'''file=open('sample.txt','a+')
file.write("\nFile operations")
file.seek(0)
print(file.read())
file.close()'''

'''file=open('sample.txt','w+')
file.write("\nFile operations")
file.seek(0)
print(file.read())
file.close()'''

'''file=open('sample.txt','r+')
file.write("\nFile operations")
file.seek(0)
print(file.read())
file.close()'''

'''#Recommended This way to write the code
with open('sample.txt','r+') as file:
    file.write("\nFile operations")
    file.seek(0)
    print(file.read())'''



'''import csv

with open('Sample.csv','r') as file:
    content=csv.reader(file)
    for row in content:
        print(row,row[0],row[1])'''


'''import csv

with open('Sample.csv','w',newline="") as file:
    writer=csv.writer(file)
    writer.writerow(['6','Bubu','PFS'])/'''


import json

with open("sample1.json","r") as file:
    data=json





1.read
2.write
3.append
4.exit
folder with 5.txt
1
name of the file
print content
2
1.rewrite=> file name,content
2.create a new file=> new name,content

3
file name
content
append




10 q/a mcq 2marks
section b
 5 -6 marks
 2 prog -25,25





 l=[1,2,3,0,0,0,2,3,0,9]
 remove zeroes from the list
 for i in l:
     if i==0:
         l.remove(i)
l=[1,2,3,0,0,0,2,3,0,9,0]
i=1
i=2
i=3

'''while 0 in l:
    l.remove(0)
print(l)'''












    
    












    

