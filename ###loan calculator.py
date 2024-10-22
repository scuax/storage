###loan calculator
amount=float(input("Enter the loan amount: "))
annual_rate=float(input("Enter the annual interest rate (as a percentage): "))
months=int(input("Enter the loan term (in months): "))
monthly_rate=annual_rate/100/12
if monthly_rate>0:
    monthly_payment=amount*monthly_rate*(1+monthly_rate)**months/((1+monthly_rate)**months-1)
else:
    monthly_payment=amount/months
print(f"The monthly payment is: ",monthly_payment,"$")