'''
#List

product=["milk","bread","sugar"]
for i in product:
    print(f"{product}-ADD TO CART|ADD TO FAV|BUY NOW")
          
#tuple

size=("s","xs","l","m","xl","xxl")
for i in size:
    print(f"....|{i}|....")

#set

followers={"meghana","sai kiran","sreee","chay"}
for i in followers:
    print(f"{i}-| unfollow|message|remove")

#Dict

data={
    "meghana":["java","python","linux"],
    "sai":["java","python","sql"],
    "sreee":["java","devops","linux"]
    }
for i in data:
    print(f"{i}:{data[i]}")

#Range

s="python programming language"
for i in s:
    print(i)

for i in range(1,11):
    print(i)

#Odd
for i in range(1,100,2):
    print(i)

#even
for i in range(2,101,2):
    print(i)

#Tables

n= int(input())
print(f"{n}-Tab;e")
for i in range(1,11):
    print(f"{n}*{i}={n*i}")

#Break

for i in range(1,11):
    if i ==4:
        break
    print(i)

#cotinue

for i in range(1,11):
    if i ==4:
        continue
    print(i)

#while

i=1
while i <=10:
    print(i)
    i=i+1


moves=12

winning_point=int(input("required steps:"))
while moves>=1:
    if moves-winning_point== moves:
        print("you won:")
        break
    print(f"{moves} are left")
    moves-=1
else:
    ("game over")



bullets=10
while bullets>0:
    print(f"you have {bullets} shoot them")
    bullets-=1
else:
    print("game over")


'''

































