"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sale=float(input("Enter Your Sale:"))
if (sale<1000):
    bouns=10/100*sale
    print("Your Bouns is:",bouns)

elif(1000>=sale):
    bouns=15/100*sale
    print("Your Bouns is:",bouns)