
n=int(input("Enter the number of students: "))

names,gpas = [],[]
max_name=''
max_val=0
min_name=''
min_val=0

for i in range(n):
    print(f"--------Student-{i+1}----------")
    name = input("Enter the name: ")
    gpa = float(input("Enter the gpa: "))
    if gpa>max_val:
        max_name=name
        max_val=gpa
    if gpa<min_val:
        min_name=name
        min_val=gpa
    names.append(name)
    gpas.append(gpa)


print(f'{"Names".ljust(15)}{"GPA".ljust(5)}')
print('-'*20)
for i in range(len(names)):
    
    print(f'({names[i].ljust(14)}|{str(gpas[i]).ljust(5)})')
    print(f"Highest gpa {max_name} -{max_val}")
    print(f"lowest  gpa {min_name} -{min_val}")
    


