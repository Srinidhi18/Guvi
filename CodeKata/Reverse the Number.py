Number = int(input())    
Rev = 0    
while(Number > 0):    
    Rem = Number %10    
    Rev = (Rev *10) + Rem   
    Number = Number //10 
print(Rev)   
