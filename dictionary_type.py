# Dictionaries uses curly braces and colons to signify the keys and their associative values
# {'key1':'value1','key2':'value2'}

my_dict={'key1':'value1','key2':'value2'}
print(my_dict['key1']);

prices_lookup = {'apple':2.99, 'oranges':3.8}
print(prices_lookup['apple'])

d = {'k1':123, 'k2':[0,1,2], 'k3':{'inside':True}}
print(d['k3'])

d['k1'] = 'New Value'
print(d)
print(d.keys())
print(d.values())
print(d.items())
