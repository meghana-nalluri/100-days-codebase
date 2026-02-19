'''
pwd=input()
if len>=8:
    s=set()
    for i in pwd:
        if i.isuppper():
            s.add("upper")
        elif i.islower():
            s.add("lower")
        elif i.isdigit():
            s.add("digit")
        else:
            s.add("splchar")
    if len(s)==4:
        print("strong password")
    else:
        print("not strong ,upper case need")
else:
    print("wrong password need to be atleast 8 characters")
