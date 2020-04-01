# Python3 program to find largest word in Dictionary 
# by deleting some characters of given string 

# Returns true if str1[] is a subsequence of str2[]. 
# m is length of str1 and n is length of str2 
def isSubSequence(str1, str2): 

	m = len(str1); 
	n = len(str2); 

	j = 0; # For index of str1 (or subsequence 

	# Traverse str2 and str1, and compare current 
	# character of str2 with first unmatched char 
	# of str1, if matched then move ahead in str1 
	i = 0; 
	while (i < n and j < m): 
		if (str1[j] == str2[i]): 
			j += 1; 
		i += 1; 

	# If all characters of str1 were found in str2 
	return (j == m); 

# Returns the longest string in dictionary which is a 
# subsequence of str. 
def findLongestString(dict1, str1): 
	result = ""; 
	length = 0; 

	# Traverse through all words of dictionary 
	for word in dict1: 
		
		# If current word is subsequence of str and is largest 
		# such word so far. 
		if (length < len(word) and isSubSequence(word, str1)): 
			result = word; 
			length = len(word); 

	# Return longest string 
	return result; 

# Driver program to test above function 

dict1 = ["ale", "apple", "monkey", "plea"]; 
str1 = "abpcplea" ; 
print(findLongestString(dict1, str1)); 
	

