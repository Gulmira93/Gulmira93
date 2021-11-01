# 09/30/2021
## lists: Looping


cars = ['bmw', 'tesla', 'lexus', 'ferrari']

"""
for tempVariable in iterative objects
   code here using tempvariable

"""
# a + b will not working here since it is  defined later


for car in cars:
    print(f'I love {car} a lot!')
    # print(f'I love {cars} a lot!')
    print('Heeey')
# scope of a carv variable is inside forloop block

print('this is my hobby.{car}')  ## this is not right way to using

a = 1
b = 3

#### SHortcut to automate : ctrl (cmd) + alt + L
########  4-1: PIZZAS#############
pizzas = ['margarita', 'grandma', 'Pepperoni', 'Mushroom']

for pizza in pizzas:
    print(f'I like {pizza} much more!')
print('I love pizzzaaaaaaa!!!!')
# shortcut : ctrl + d > duplicating the line that your cursor on
# shortcut : ctrl + y > delete the line that your cursor on
# shortcut: ctrl + alt(cmd) + up/down  > dragging and dropping the line

print('####################  4-2:  Animals ###############')
animals = ['horse', 'dog', 'cat']
for animal in animals[:]:
    print(f' A {animal} will make a great pet!')
print("any of these animalwill make y a great pet")


### Slicing the list name_of_the_list[startIndex:EndingIndex]
#   - this means creating sublist from startIndex element (inclusive) to endindex -1 (excluding endindex element)
# name_of_the_list[:] - from the start to end of the list


## copying the list:
copy_animals = animals
print(f'copy_list: {copy_animals}')
print(f'animals list: {copy_animals}')


copy_animals.append('snake')


























