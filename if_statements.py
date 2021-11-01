# If statements
# yes/no (True/False)
# 5 == 4 >> False
# 25 > 15 >> true

# 'a' in 'car' -> true coz a is second letter in car
# 'b' in 'car' -> false # coz no b letter in car word

a = 20
b = 'john'
# a == 20 -> True
# a == 30 -> false
# b.upper() == 'JOHN'

nums = [3, 8, 9, 80]
# 5 in nums  -> FALSE

print(5 in nums)
print(8 in nums)

# Admission for anyone under age 4 is free
# Admission


age = 5

if 4 < age <= 18:
    print('Your admission fee is free.')
elif age <= 18:
    print('Your admission fee is $5.')
else:
    print('your admission fee is $10.')

print('################## 5-3 #############')
alien_color = 'red'
if alien_color.lower() == 'green':
    print('you can just earned 5 points , yahoo!!!')
elif alien_color.lower() == 'yellow':
    print('you just earned 10 points,great!!')
elif alien_color.lower() == 'red':
    print('you just earned 30 points, super!!!')
else:
    print('you havenot just earned any points, keep trying...!!!!')
alien_color = input('Enter the color of alien you shot: ')

#  create list of numbers from 1 to 100 that can be
# dividable 3 (listBy3),
# dividable 3 (listBY5)
# dividable 3 and 5 (listBy35)
# % - MODULO REMAINING AFTER DIVIDING
# EX:
###############NUMBERS##############
listby3 = []
listby5 = []
listby35 = []
for num in range(1, 101):
    print(num)
    if num % 3 == 0:
        listby3.append(num)
    elif num % 5 == 0:
        listby5.append(num)
    elif num % 3 == 0 and num % 5 == 0:
        listby35.append(num)

print(listby3)
print(listby5)
print(listby35)

#### H/W FuzzBuzz exercise:
# accept the input , if you see input




print("##################Multiplication table######################################")
nums1 = range(1, 11)
nums2 = range(1, 11)
for row in nums2:
    for col in num2:
        print(f"\t{col}*{row}={row*col}", end='\t')
    print()


































