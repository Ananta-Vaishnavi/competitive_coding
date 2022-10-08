#User function Template for python3
class Solution:

	def findMaximum(self,arr, n):
		def Greatest(arr):
		    left=0
		    right=len(arr)-1
		    while left<=right:
		        mid=(left+right)//2
		        if mid<len(arr) and mid-1>0:
		            if arr[mid]<arr[mid-1]:
		                    right=mid-1
		        if mid+1<len(arr) and mid>0:
		            if arr[mid]<arr[mid+1]:
		                    left=mid+1
		        if mid+1<len(arr) and mid-1>0:
		            if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
		                return arr[mid] 
        return Greatest(arr)
