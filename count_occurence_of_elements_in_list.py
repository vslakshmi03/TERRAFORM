list = ['This', 'is', 'an', 'apple', 'apple', 'is', 'very', 'good']
print([[x,list.count(x)] for x in set(list)])
