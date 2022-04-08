l=int(input())
n=int(input())
def photo(w,h):
  if w<l or h<l:
    print('UPLOAD ANOTHER')
  elif w==h:
    print('ACCEPTED')
  elif w>l or h>l:
    print('CROP IT')
for i in range(n):
  w,h=input().split()
  w=int(w)
  h=int(h)   
  photo(w,h)
