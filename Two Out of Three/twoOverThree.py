from decimal import *

def Pk (k):
    result = 1
    getcontext().prec = 15
    for num in xrange(2,k+1):
        result *= Decimal(num**3.00-1)/Decimal(num**3.00+1)
    return result
    
k = 4470

while True:
    if Pk(k) < 0.6666667:
        break
    k += 1
        
        
print k-1, Pk(k-1)
