f1 = open("output.txt", "w")
with open("test_file.txt", "r") as myfile:
    data =myfile.read()
data_1 =data[::-1]
f1.write(data_1)
f1.close()
