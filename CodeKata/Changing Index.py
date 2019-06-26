a=int(input())
c=list(map(int,input().split()))
for i in range(len(c)):
    if c[i]>c[i+1]:
        break
print(i)
