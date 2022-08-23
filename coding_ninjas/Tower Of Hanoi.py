import sys
sys.setrecursionlimit(10**6)
def TowerOfHanoi(n,a,b,c):
    if n==0:
        return
    TowerOfHanoi(n-1,a,c,b)
    print("Disk {} moved from {} to {}".format(int(n),a,c))
    TowerOfHanoi(n-1,b,a,c)
n=int(input())
TowerOfHanoi(n,'A','B','C')
