from collections import OrderedDict
def remove_string(str):
   return "".join(OrderedDict.fromkeys(str))
print(remove_string("this is test"))
