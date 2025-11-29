principle_amt=float(input("enter the amount"))

rate =0.05 #5%

for i in range(1,11):
    a=principle_amt*(1+rate)**i
    print(f"{a:2f}")
    