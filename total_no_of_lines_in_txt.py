file_path = "hello.txt"
lines_count = 0
with open(file_path,'r') as f:
  for l in f:
    lines_count = lines_count +1
print("Total number of lines : ",lines_count)
