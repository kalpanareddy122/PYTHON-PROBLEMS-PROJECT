rainsize=int(input("enter rainsize in mm:"))
#int(),#float(),#str(),#bool()
if rainsize<1 and rainsize>=0:
    print("no rain")
elif rainsize>=1 and rainsize<5:
    print("light rain")
elif rainsize>=5 and rainsize<10:
    print("moderate rain")
elif rainsize>=10:
    print("heavy rain")
else :
    print("invalid input")