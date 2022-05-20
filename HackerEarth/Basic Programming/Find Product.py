m=10**9+7
a=int(input())
l=[int(i) for i in input().split()]
ans=1
for i in l:
  ans=ans*i%m
print(ans)
