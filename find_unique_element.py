# Python 3 program to find unique element where 
# every element appears k times except one 
import sys 

def findUnique(a, n, k): 
	
	# Create a count array to store count of 
	# numbers that have a particular bit set. 
	# count[i] stores count of array elements 
	# with i-th bit set. 
	INT_SIZE = 8 * sys.getsizeof(int) 
	count = [0] * INT_SIZE 
	
	# AND(bitwise) each element of the array 
	# with each set digit (one at a time) 
	# to get the count of set bits at each 
	# position 
	for i in range(INT_SIZE): 
		for j in range(n): 
			if ((a[j] & (1 << i)) != 0): 
				count[i] += 1

	# Now consider all bits whose count is 
	# not multiple of k to form the required 
	# number. 
	res = 0
	for i in range(INT_SIZE): 
		res += (count[i] % k) * (1 << i) 
	return res 

# Driver Code 
if __name__ == '__main__': 
	a = [6, 2, 5, 2, 2, 6, 6] 
	n = len(a) 
	k = 3
	print(findUnique(a, n, k));
