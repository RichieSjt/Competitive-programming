  
def isPrime(num):

    if num > 1:  
        for i in range(2, num):     
            if (num % i) == 0: 
                return False
                break
        else: 
            return True
    else: 
        return False

num = input()
counter = 0
prime = False
primes = list()
counter = 0
        
numeros = [int(i) for i in str(num)]

for i in range(len(numeros)):
    temp = numeros[i]
    while(not prime):
        if(isPrime(temp)):
            primes[counter] = temp
            print(counter)
            counter += 1
            prime = True
        else:
            temp = int(str(temp) + str(numeros[i+1]))
            i += 1

if (counter != 3):
    print("Bob lies")
else:
    print(primes[0]*primes[1]*primes[2])        

