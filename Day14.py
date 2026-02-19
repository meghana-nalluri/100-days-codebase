'''
               ******************READ********************
               
file=open("sample.txt","r")
construct1=file.read()
file.seek(0)
construct2=file.readline()
file.seek(0)
construct3=file.readlines()
print(construct1,construct2,construct3,seq='/n/n')
file.close

               *********************WRITE********************

file=open("samples.txt","w")
file.write("Hello People...")
file.close()

            *****************APPEND*****************************

            
file=open("samples.txt","a")
file.write("/nHello People...")
file.close()

             *****************READ + WRITE +APPEND***********************


file=open("samples.txt","r+")
file.write("/nHello People...")
file.seek(0)
print(file)
file.close()



file=open("samples.txt","w+")
file.write("/nHello People...")
file.seek(0)
print(file)
file.close()


        *****************AS FILE**********************
with open ("sample.txt","r") as file:
    file.wwrite("/nFile "
)





with open("sample.txt","w") as file:
    file.write("override")


with open("sample.txt","a") as file:
    file.write("override")

with open("sample.txt","r") as file:
    content=file.read()
    print(content)



