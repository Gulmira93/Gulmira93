                                                                # data structure - to handle complex data ke
# key : value, {'key': 'vaulue1', 'key:' 'value2','key3': 'value3' }


student1 = {'name': 'steven',
            'age': 25,
            'city': 'Brooklyn'}

student1_list = ['Steven', 25, 'Brooklyn']

print('from the list: ', student1['name'])

########Adding element to the dictionary######
student1['country'] = 'USA'
print(student1)
print(sorted(student1)) # returns sorted list of keys, temp list
print(type(student1)) # returns sorted list of keys, temp list
print(type(student1_list)) # returns sorted list of keys, temp list

# REMOVING DUPLICATES
nums = [1, 3, 5, 3, 3, 3, 3, 3, 3, 9, 9]
print(nums)
nums_set = set(nums)
print(nums_set)
u_nums = list(nums_set)
print(u_nums)
# ########SETS IN PYTHON
# customers, city ; suppliers, city
# get the cities where you have customers and suppliers

#select city from customers
#intersect
#select city from suppliers

# get the cities with only customers where you have customers and suppliers
# select cities from customers
#except
# select city from suppliers
set1 = {3, 4, 6, 7, 20, 45}
set2 = {1, 2, 9, 5, 3, 36}
print('union:', set1.union(set2))
print('difference:', set1.difference(set2))
print('intersection:', set1.intersection(set2))





#############Dictionaries ######
# post
post = {'user_id': 209, 'message': 'D5, K9, O9, 23K ', 'location': (142.888755, -189.098), 'datetime': '0721199302ls', 'language': 'english'}
post2 = dict(message='SS Cotopaxi', language='english')

if 'location' in post2:
    print(post2['location'])
else:
    print('Post2 does not contain a location value.')


post2['user_id'] = 908
post2['datetime'] = '290489057ihdjcdm'
post2['location'] = '123.998, -123.09'
print(post2)

try:
    print(post2['location'])
except KeyError:
    print('Post2 does not have a location value')

print('##########Modifiying values in Dictionary')

student1['age'] = 27
print(student1)
#student1['age'] =student1['age'] + 2
student1['age'] += 2
print(student1)
print('###### Removing the Key-value pair from dictionary')
student1 ['ages'] = 28
print(student1)
del student1['ages']
print((student1))


print('#### Looping the dictionaries')
# by default (base on keys)
# by keys
# by value
# by keys,values














