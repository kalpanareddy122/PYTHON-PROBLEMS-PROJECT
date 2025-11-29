price=input("enter the price of the movie ticket:")
price=float(price)
number_of_tickets=int(input("enter number"))
category=int(input("enter 1 for student\n" ))
if number_of_tickets>15 and category==1:
    total_price=(number_of_tickets*price)*0.75
    print("the discount: ", total_price)
elif number_of_tickets>15 and category!=1:
    total_price=(number_of_tickets(price))*0.8
    print("The discount:",total_price)
elif number_of_tickets<=15 and category==1:
    total_price=number_of_tickets*price
    print("the total price:",total_price)

