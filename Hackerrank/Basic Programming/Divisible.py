n=int(input())
a=int(n/2)
s=''
lst = [item for item in input().split()]
#print(lst)
for i in range (a):
  s1=(lst[i][0])
  s=s+s1
for _ in range (a,n):
  s2=(lst[_][-1])
  s=s+s2
s=int(s)
if s%11==0:
  print('OUI')
else:
  print('NON')
