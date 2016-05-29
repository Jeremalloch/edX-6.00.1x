#balance = 320000
#annualInterestRate = 0.2
monthlyInterest=annualInterestRate/12.0
mpLower= balance / 12
mpUpper= (balance *(1 + monthlyInterest)**12) / 12.0
balanceCopy = balance
while abs(balance) > 0.001:
    balance = balanceCopy
    payment=(mpLower+mpUpper)/2
    for month in range(1,13):
        unpaidBalance=balance-payment
        balance=unpaidBalance+round((annualInterestRate/12)*unpaidBalance,2)
    if balance>0:
        mpLower=payment
    elif balance<0:
        mpUpper=payment
payment=round(payment,2)
print('Lowest Payment: '+str(payment))