text = "Hello how are you"

new_text = text.split(" ")
print(new_text)

reverse= [ ]
for text_reverse in new_text[::-1]:
    print(text_reverse)
    reverse.append(text_reverse)
print(reverse)    

