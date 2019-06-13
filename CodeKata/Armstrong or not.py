
def arms():
  sum = 0
  t = a
  while t > 0:
    c = t % 10
    sum += c ** 3
    t //= 10          
  if a == sum:
    print('yes')
  else: 
    print('no')
a=int(input()) 
if(a<=100000):
  arm()  


      
  
