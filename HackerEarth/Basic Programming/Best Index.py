# for square root function
import cmath
sum=0
s=[]
n=int(input())
l=[int(_) for _ in input().split()]
max_num=0
#finding n i n the formula n*(n+1)/2
d = 1 + (4*2*n)
sol =(-1+cmath.sqrt(d))/(2)
x=(int(sol.real))
max_num=int(x*(x+1)/2)
for i in range (0,n):
  if n-i<max_num:
    x-=1
  else:
    pass
  max_num=int(x*(x+1)/2)
  #print(max_num)
  sum=0
  for j in range(i,i+max_num):
    sum+=l[j]
  s.append(sum)
print(max(s))
