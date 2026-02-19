''''
def Calc(a,b):
    sum_val=a+b
    diff_val=a-b
    mul_val=a*b
    return sum_val,diff_val,mul_val
    
result_add,result_diff,result_mul=Calc(3,4)
print(f"addition of a and b is {result_add} {result_diff} {result_mul}")
'''
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a*b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
exp=inpt("enter the exp:")
for i in expo:
    if i=="+":
        a,b=exp.split("+")
        print(add(int(a),int(b)))
    elif=="-":
        a,b=exp.split("-")
        print(sub(int(a),int(b)))
    elif=="*":
        a,b=exp.split("*")
        print(mul(int(a),int(b)))
