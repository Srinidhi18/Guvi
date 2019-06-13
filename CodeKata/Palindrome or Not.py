a = int(input()) 
t = a
rev = 0
while t != 0:
	rev = (rev * 10) + (t % 10)
	t = t // 10
if a == rev:
	print("yes")
else:
	print("no")

