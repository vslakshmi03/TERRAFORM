list = [1, 2, 3, 4, 5, 6]
list_2 = [8, 9, 10]
list_3 = [11, 12, 13, 14]
print(list)
print(*list)
print(*list, sep = ", ")
print(*list, sep = " \n")
list.append(7)
print(list)
list.extend(list_2)
print(list)
final_list = list+list_2+list_3
print(final_list)
reverse_list = final_list[::-1]
print(reverse_list)

