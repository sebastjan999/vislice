#Napisi ptogram, ki izpise vsa prastevila manjsa od 200

def je_prastevilo(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

for x in range(2,201): 
    if je_prastevilo:
        print(x)   
        lol
