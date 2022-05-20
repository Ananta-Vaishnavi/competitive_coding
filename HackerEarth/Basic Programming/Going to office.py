d=int(input())
oc,of,od=input().split()
cs,cb,cm,cd=input().split()
online=int(oc)+(d-int(of))*int(od)
classic=int(cb)+int(d/int(cs))*int(cm)+d*int(cd)
if online<=classic:
  print("Online Taxi")
else:
  print('Classic Taxi')
