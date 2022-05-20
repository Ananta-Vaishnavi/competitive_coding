count=0
l,r,k=input().split()
l=int(l)
r=int(r)
k=int(k)
count=0
for x in range(l,r+1):
  if x%k==0:
    count+=1
print(count)
