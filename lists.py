# Lists  (Array)
num = list()
even = []  # these are 2 ways to create an empty list!
# operations: creating , access, add element , copy, remove element
odds = [1, 3, 5, 7, 9, 457]
num = 44
# index:0 1 2 3 4 5
# negative index: -6  -5 -4 -3 -2 -1
# 5 element , size of 'odds' list is 5
# what is the element on index 2? it is 5 ,coz indexing starts with zero 0
friends = ['jackson', 'said', 'akmal', 'lenur']
# Access
first_friend = (friends[0])
print(f"friends: {friends}")
print(f"first_friend: {first_friend}")
print(f"friends[0]: {friends[0].title()}")
print(f"friends[1]: {friends[1]}")
print(f"friends[2]: {friends[2]}")
print(f"friends[3]: {friends[3]}")
#    print(f"friends[3]: {friends[3]}");IndexError: list index out of range

print(
    f"friends[-1]: {friends[-1]}")  # look at the the right side of your list, negative indexes starting from the last element
print(f"f odds[-3]: {odds[-3]}")

# Adding elements :
# list.append(new element) -- this adds new_element to the end of the list
# list_insert(index, new_element) - this adds new_element on the indicated index,shifts all elemnts to right
# add a friend : Obama to a friend list
friends.append('Obama')
print(f"new friends list: {friends}")
friends.insert(0, 'messi')
print(f"new friends list after insert: {friends}")
# resetting the exsistinge element , only exisisting index should be used.IndexError:

friends[2] = 'mark'
print(f"new_friends list after reset: {friends}")
# friends[7]= 'elon'#IndexError: list assignment index out of range
# print(f"new_friends list after adding new: {friends}")
# to comment do ctrl + /

# Remove the elements: by value, index
friends.remove('mark')
# removed_one1=friends.remove('mark') - this not valid statement, since remove() does not return anything
# print (removed_one1)
print(f"new friends list after removing 'mark': {friends}")


friends.pop(4)  # pop() function returns (informs) what it is removing
print(f"new friends list after popping index 4: {friends}")
friends.pop(1)
print(f"new friends list after popping index 1: {friends}")
removed_friends = []
#removed_one = friends.pop(4) # pop() function returns (informs) what it is removing
#print(removed_one)
print(f"new friends list after popping index 4: {friends}")

# RETURN HAS A VALUE
# REMOVE DOESN NOT RETURN ANYTHINg
del friends[-1]
print(f"new friends list after del index -1: {friends}")
friends[]
print(f"new friends list after redifining: {friends}")






