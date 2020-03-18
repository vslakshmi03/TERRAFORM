given_str = input("Give me a string: ")
str_dic = {}
for i in given_str:
    if i not in str_dic:
        str_dic[i] = 0
    str_dic[i] = str_dic[i]+1

for i,j in str_dic.items() :
    if str_dic[i] > 1:
      print(f'{i} is a duplicate char')
        
print(str_dic)  
