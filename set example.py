'''
s=["audio.mp3","photo.png","nature.png"]
voice=[]
pics=[]
for files in s:
    if files.endswith(".mp3"):
        voice.append(files)
    if files.endswith(".png"):
        pics.append(files)
print("you select audio file:",voice)
print("you select audio file:",pics)

                      ********************************

data= {
    'praveen@gmail.com':'Pr@123',
    'varsha@gmail.com':'Vs@098',
    'sapnil@gmail.com':'Sp@789',
    'saaketh@gmail.com':'St@456',
    'sanjana@gmail.com':'Sn@678'
 }

print('1.Register')
print('2.Login')

ch = int(input("Enter your choice: "))

if ch==1:
    email=input("Enter the email: ")
    pwd = input("Enter the password: ")
    if email in data:
        print(f"Register - Failed\n{email} is already exist ")
    else:
        data[email]=pwd
        print("Registered Successfully")

elif ch==2:
    email=input("Enter the email: ")
    pwd = input("Enter the password: ")
    if email in data and data[email]==pwd:
        print(f"Login Successful")
    else:
        print("Invalid Login")

    
else:
    print("Enter the valid choice")

'''

























    
