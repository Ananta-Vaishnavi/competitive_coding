def cost(): 
  c=input().split() 
  n=int(input())
  c1=int(c[0]) 
  c2=int(c[1]) 
  c_min=min(c1,c2) 
  c_max=max(c1,c2) 
  a1=0 
  a2=0
  for i in range(n):
    a=input().split() 
    a1+=int(a[0])
    a2+=int(a[1]) 
    a_min=min(a1,a2)
    a_max=max(a1,a2)
  print(c_min*a_max+c_max*a_min)
t=int(input())
for tr in range(0,t):
  cost()
