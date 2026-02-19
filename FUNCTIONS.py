def student_data(info):
    print(f'name:{info[0]}')
    print(f'cource:{info[1]}')
    print(f'g_year:{info[2]}')
    print(f'----END-----')
    print("\n\n")
data=[["meghana","MCA","2025"],
      ["sai","BTECH","2025"],
      ["sreee","MCA","2024"]]
for i in data:
          student_data(i)


                     #***********
                     
def display(uname,email,password,status="absent"):
    print(f'username:{uname}')
    print(f'email:{email}')
    print(f'password:{password}')
display("sai kiran","sai1@gmail.com","SAi@12345","present")

#key word arguments

display(username="sai kiran",email="sai1@gmail.com",password="SAi@12345")

                    **********************

def display(*names):
    for i in names:
        print(i)
    else:
        print("______________END OF THE LIST-----------------")
display("gaya")
display("sai kiran","chandu","chaithanya")
display("sreee","meghana")

                   ********************************



    
    




















