x=input()
j=[]
for i in x:
  if i.isnumeric():
    j.append(i)
print("".join(j))
