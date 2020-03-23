# library that handles the URL stuff 
import urllib.request 

# Importing module required for 
# regular expressions 
import re 

# Assign urlopen to a file object variable 
fhand = urllib.request.urlopen('https://amplitude.com/contact?ref=footer') 

for line in fhand: 
    # Getting the text file 
    # content line by line. 
    s = line.decode().strip() 

    # regex for extracting all email-ids 
    # from the text file 
    reg = re.findall(r"[A-Za-z0-9._%+-]+"
                    r"@[A-Za-z0-9.-]+"
                    r"\.[A-Za-z]{2,4}", s) 

    # printing the list output 
    print(reg) 


