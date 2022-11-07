import time 
import os

n = int(input("Enter Number of Rows = "))
m = int(input("Enter Number of arrows line = ")) 

for i in range(n) :
    for j in range(n-i-1):
        print(" ",end="" )
    for j in range(i+1):
        print("*",end=" " )
    print()  
    
for i in range(m):
    for j in range(n-1):
        print(" ",end="" )
    print("*",end=" ")
    print()       
time.sleep(1) 
os.system("cls")    
   
for i in range(m):
    for j in range(n-1):
        print(" ",end="" )
    print("*",end=" ")
    print()   
    


for i in range(n) :
    for j in range(i):
        print(" ",end="" )
    for j in range((n-i)):
        print("*",end=" " )
    print()  
time.sleep(1) 
os.system("cls")  

   

