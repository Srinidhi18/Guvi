a,b=map(int,input().split())

for i in range(a,b):   
   sum = 0
   t = i
   while t > 0:
       c = t % 10
       sum += c ** 3
       t //= 10
   if i == sum:
       print(i, end=' ')
