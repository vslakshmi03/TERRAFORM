dicts = {'name':'swarna', 'age':27, 'class':'masters', 'city':'sfo'}
print(dicts)
print(dicts.keys())
print(dicts.values())
dicts.update({'hubby':'phani'})
print(dicts)
#new = dict((v, k) for k, v in dicts.iteritems())
new = dict(map(reversed, dicts.items()))
print(new)
#reverse = {value: key for key, value in dicts.iteritems()}
#print(reverse)