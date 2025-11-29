digit_words=[
    "zero","one","two","three","four","five","six","seven","eight","nine"]

number=input("enter the number:")

for i in number:
    print(digit_words[int(i)],end="")