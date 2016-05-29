balance = 4213
annualInterestRate = 0.2
payment=0
n=0
balancelist=[balance]
while balancelist[n]>0:   
    payment+=10
    xbalance=balance
    for month in range(1,13):
        unpaidBalance=xbalance-payment
        interest=round((annualInterestRate/12)*unpaidBalance,2)
        xbalance=unpaidBalance+interest
        #print('Month: ' + str(month))
        #print('Payment: '+str(payment))
        #print('Remaining balance: ' + str(xbalance))
    balancelist.append(xbalance)
    #print(n)
    #print(balancelist[n])
    n+=1
print('Lowest Payment: '+str(payment)) 