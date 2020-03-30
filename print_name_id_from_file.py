### Program to read from a file and print unique names and unique websites and user read websites.

line_split_list = []
names_list = []
websites_list = []
tmp_websites_list = []
with open("file.txt","r") as file_pointer:
    for line in file_pointer:
        line_split_list = line.split(" ")
        if line_split_list[0] in names_list:
            print()
        else:
            names_list.append(line_split_list[0])
        tmp_websites_list = line_split_list[2].split(".")
        if tmp_websites_list[0] == "www":
           if tmp_websites_list [1] in websites_list:
               print()
           else:
               websites_list.append(tmp_websites_list [1])
        else:
            if tmp_websites_list[0] in websites_list:
                print()
            else:
                websites_list.append(tmp_websites_list[0])


print (websites_list)
print (names_list)



