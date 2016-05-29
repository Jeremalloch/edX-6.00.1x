#balance - the outstanding balance on the credit card
#annualInterestRate - annual interest rate as a decimal
#monthlyPaymentRate - minimum monthly payment rate as a decimal
#Month: 1
#Minimum monthly payment: 96.0
#Remaining balance: 4784.0
#balance = 4213
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04
minimumPaymentTotal=0
for month in range(1,13):
    minimumPayment=round(balance*monthlyPaymentRate,2)
    unpaidBalance=balance-minimumPayment
    interest=round((annualInterestRate/12)*unpaidBalance,2)
    balance=unpaidBalance+interest
    print('Month: ' + str(month))
    print('Minimum monthly payment: '+ str(minimumPayment))
    print('Remaining balance: ' + str(balance))
    minimumPaymentTotal+=minimumPayment
    remamingBalance=balance
print('Total paid: '+str(minimumPaymentTotal))
print('Remaining balance: '+ str(remamingBalance))