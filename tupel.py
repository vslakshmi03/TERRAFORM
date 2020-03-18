tuple = (1, 2, 3, 4, 5)
print(tuple)
tuple = tuple + (6,)
print(tuple)
tuple_1 = (7, 8, 9, 10)
final_tuple = tuple + tuple_1
print(*final_tuple)
reverse_tuple = final_tuple[::-1]
print(reverse_tuple)

