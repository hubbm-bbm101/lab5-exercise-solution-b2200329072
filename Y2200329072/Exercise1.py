N = int(input("Enter number="))
Oddtotal=0
Eventotal=0
Evenaverage=0
for number in range(1,N+1):
    if(number %2!=0):    
     Oddtotal= Oddtotal+ number
    
for number in range(1,N+1):
    if(number %2 !=1):
                
     Eventotal= Eventotal+ number
    Evenaverage = Eventotal//(2*N)
         
print("The sum of Odd numbers from 1 to", N, "is",Oddtotal)
print("The average of Even numbers from 1 to", N, "is",Evenaverage)
