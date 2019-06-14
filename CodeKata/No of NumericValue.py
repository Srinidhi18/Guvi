a=input()
c=0
if len(a) <= 1000 :
  for i in range (len(a)):
    if(a[i].isdigit()):
      c=c+1
  print(c)
