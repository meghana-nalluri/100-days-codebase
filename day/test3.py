'''d={"Arjun":85,"Rahul":90,"Anita":78}
name=input("Enter student name:").strip()
try:
    print(d[name])
except KeyError:
    print("student not found")'''

'''s1=set(map(int,input("Enter set1:").split()))
s2=set(map(int,input("Enter set2:").split()))
print(f"Union:{s1|s2}")
print(f"Intersection:{s1&s2}")
print(f"Difference:{s1-s2}")'''

'''try:
    with open('data.txt','r') as file:
        print(len(file.readlines()))
except FileNotFoundError:
    print("data.txt does not exist")'''



'''import json
with open('demo.json','w') as file:
    data=[
        {'title':'Python Basics','author':'John Doe','price':1499}
        ]
    json.dump(data,file,indent=4)
with open('demo.json','r') as file:
    print(json.load(file))'''

'''try:
    data={"a":1,"b":2}
    print(data["c"])
except KeyError:
    print("Key not found")'''

'''try:
    file=open("data.txt","r")
    print(file.read())

except FileNotFoundError:
    print("File is not present")'''

'''import operations
print(operations.add(6,7))
print(operations.sub(6,7))
print(operations.mul(6,7))
print(operations.div(6,7))'''


'''import operations as op
print(op.add(6,7))
print(op.sub(6,7))
print(op.mul(6,7))
print(op.div(6,7))'''


from operations import add,sub#need few things
print(add(6,7))
print(sub(6,7))


































