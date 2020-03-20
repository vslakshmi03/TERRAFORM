filepath = 'file1.txt' 
with open(filepath, 'r') as file_pointer:
     line = file_pointer.readline()
     new_file_pointer = open("file2.txt", "a")
     while line:
         print(f'{line}')
         new_file_pointer.write(f"sampletext {line}")
