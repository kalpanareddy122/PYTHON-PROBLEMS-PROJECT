num = input("enter the 5 digit number:")

if len(num) != 4 or not num.isdigit():
    print("invalid")
else:
    digits=[int(i) for i in num] #converting to int

    increasing = all(
        digits[i]+1==digits[i+1]
        for i in range(3)
    )
    decreasing = all(
        digits[i]-1==digits[i+1]
        for i in range(3)
    )
    if increasing==True:
        print("increasing fancy number")
    elif decreasing==True:
        print("decreasing fancy number")
    else:
        print("not fancy number")
