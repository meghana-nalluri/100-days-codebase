def Calc(a,b):
    sum_val=a+b
    diff_val=a-b
    mul_val=a*b
    return sum_val,diff_val,mul_val
    
result_add,result_diff,result_mul=Calc(3,4)
print(f"addition of a and b is {result_add} {result_diff} {result_mul}")
