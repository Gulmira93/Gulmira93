# 03/04/2021   String(str)
# string is a sentence, character, number, a word as a character that
# represents character !
fullname= 'jon doe'
msg="we are looking at string functions in python."
#print (fullname)
#print (fullname.upper())
#print(msg.lower())
#print(fullname.title())
#print(msg.replace('.', '!!!!!!!').title())
#print(msg.replace('python', 'java'))
print(f"fullname.isdigit() >> {fullname.isdigit()}")
print(f"fullname.isdigit() >> {fullname.islower()}")
print(f"fullname.isdigit() >> {fullname.isupper()}")
print(f"fullname.isdigit() >> {fullname.istitle()}")
print(f"467.isdigit() >> {'467'.istitle()}")

#Concatenation
msg1 = fullname + ',' + msg
msg1 = fullname  + '$$$$$$' + msg
print (msg1)
msg1 = fullname.title() + "," + msg
print(msg1)
print(fullname.upper() + "," + msg)

#  working with whitespaces in string: \t, \n, etc
msg2 = fullname.upper() + "\n,\t,\t,\t, " + msg
print (msg2)
msg2= (fullname.replace ("\t", '' )) + msg
print (msg2)
msg3 ='\n\t\t\t' + fullname.upper() + "," + msg
# str.strip() - removes leading and preceding whitespaces
print(msg3 + '!!!')
print(msg3.strip() + '!!!')

#fstring
msg3= fullname.upper() + "," + msg
msg4= f"{fullname.upper()} , {msg}  ddhfk,,kyftrseesjd"
msg5= f"{fullname.title()}, {msg}"
print(msg5)
print("fstring")
print(msg4 + '!!!')

last_name = f"BRown"

print("Integers:***********************8")
num = 234
num2 = 399
#print=(num.strip())
#strip is only using for string data type , not integer(num)
message = "one of python's strengths  is its diverse community."
print (message)
print(f"num+num2 = {num+num2}")
print(f"num-num2 = {num-num2}")
print(f"num*num2 = {num*num2}")
print(f"num/num2 = {num/num2}")

#str (expression) - this will convert+ the data type to str
print("Value of num is : " + str(num))
print("num + num2 = " + str(num + num2))

num3 = "248" # it is string not integer (int)
print(f"num + num3 = {num + int(num3)}")

# ctrl + click - will take you  where specific variable is defined.
print(f"3**2 = {3**2}") # 3**2 means 3*3 , or square of 3, '**' means exponents

num4 = "34.37"
print("num+num4 = " + str(num+num4))
print(f"num + num2 = {num  + float(num4)}")


print(int(45.5679))


# Exercises 2-5;
print("# Exercises 2-5;")
quote = '\t\t\tAlbert Einstein once said, “A person who never made \n \t\t\ta mistake never tried anything new.”'
print(quote)
author="Albert Einstein"
quote = f'\t\t\t {author}  once said, “A person who never made \n \t\t\ta mistake never tried anything new.”'
print(quote)

#Homework: all in chapter 2.

#2-1.
msg="I'm learning python."
print(msg)
msg="python is not easy for me."
print(msg)


num5 = "567"
print(f"num+num5 = {num+int(num5)}")
num6 = 36.67
print(f"num+num6 = {num+float(num6)}")





















































































































