#Python3 program for finding
#number of divisor 

#program for finding
#no. of divisors 
def divCount(n):
    #sieve method for 
    #prime calculation
    hh = [1] * (n+1)
    
    p = 2 
    while ((p * p) < n):
        if (hh[p] == 1):
            for i in range((p*2), n, p):
                hh[i] = 0
        p += 1 
        
        
    #Traversing through all prime numbers 
    total = 1 
    for p in range(2, n+1):
        if (hh[p] == 1):
            #calculate number of divisor 
            #with formula total div = (p1+1) * (p2+1) * ... * (pn+1)
            #where n = (a1^pn) ai being prmie divisor 
            #for n and pi are their respective 
            #power in factorization
            count = 0
            if (n%p == 0):
                while(n%p == 0):
                    n = int(n/p);
                    count += 1 
                total *= (count+1);
    return total;
    

listOfDivisor = [] 
numberForLoop = int(input("Enter number of loop: "))
for i in range(numberForLoop):
    dict = {}
    number = int(input("Enter number: "))
    divisor = divCount(number)
    dict['number'] = number
    dict['divisorCount'] = divisor
    listOfDivisor.append(dict)
    

maxDivisor = max(listOfDivisor, key = lambda x:x['divisorCount'])

print(listOfDivisor)
print('\n')
print(maxDivisor)