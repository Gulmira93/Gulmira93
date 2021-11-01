
# None - zero / null in python
# null - zero in sql
from functions import *
def describe_city(city,country="United states of america"):
    print(f'{city.title()} is in {country.upper()}')
describe_city('new york')
describe_city('paris', 'france')
describe_city('brooklyn')
describe_city('dubai', 'UAE')

print ('############### 8-7: Album ###############')
def make_album(artist_name, album_title):
    album ={'Artist': artist_name, 'album': album_title}
    return album
album1 = make_album('aracde fire', 'funeral')
album2 = make_album('Shakira', 'diitfdg')
print(album1, album2)
print(f"{album1['Artist']}had a great album named  {album1 ['album']}")
print(f"{album2['Artist']}the best album in 2019 {album2['album']}")


# H/w : 8-9, 8-10, 8-11
# hw : Palindrome . create a functions that tell if the word is palindrome or not
# return True if palindrome False if it is not palindrome
# you might need for loop and if condition
def is_palendrome(word):
    result = None
    return result






















































































































