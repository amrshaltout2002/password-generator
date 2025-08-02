"""
1.import string module
2.store all characters in lists (upper/lower case, digits, punctuations)
3.take number of characters from user
4. make sure the number of characters greater than or equal 8
5.shuffle all lists
6.calculate 30% and 20% of number of characters
7.create password 60% letters and 40% digits and punctuations
"""

import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

characters_number = input("Number of characters in your password: ")

while True:
  try:
    characters_number = int(characters_number)
    if characters_number < 8:
      print("you need at least 6 characters")
      characters_number = input("please enter the number again: ")
    else:
      break
  except:
    print("enter numbers only")
    characters_number = input("Number of characters in your password: ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))

password = []

for i in range(part1):
  password.append(s1[i])
  password.append(s2[i])

for i in range(part2):
  password.append(s3[i])
  password.append(s4[i])

random.shuffle(password)
password = "".join(password[:])
print(password)