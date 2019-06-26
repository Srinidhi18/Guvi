c=list(input())
if(len(c)%2==0):
	c[int(len(c)/2)]="*"
	c[int(len(c)/2)-1]="*"
else:
	c[int(len(c)/2)]="*"
for i in range(0,len(c)):
	print(c[i],end="")
