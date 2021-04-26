#https://practice.geeksforgeeks.org/problems/sum-of-product-of-x-and-y-with-floornx-y3711/1/?category[]=Mathematical&category[]=Mathematical&page=1&query=category[]Mathematicalpage1category[]Mathematical#


import math
class Solution:
	def sumofproduct(self, n):
		# Code here
		summ=0
		for i in range(1,n+1):
		    summ+=(i*(n//i))
		return summ