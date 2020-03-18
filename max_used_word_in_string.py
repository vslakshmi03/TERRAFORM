test_list = 'apple mango apple'
new_list = test_list.split(" ")
  
# printing original list 
print ("Original list : " + str(new_list)) 
  
# using naive method to  
# get most frequent element 
max = 0
res = new_list[0] 
for words in new_list: 
    freq = new_list.count(words) 
    if freq > max: 
        max = freq 
        res = words
      
# printing result 
print ("Most frequent number is : " + str(res)) 
