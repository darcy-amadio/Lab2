#Question 1

print('input a binary number')
binary_num = str(input()) 
decimal_num = 0
power = 0
x = 0 # this variable represents the string index number
while binary_num != 0 :
  decimal_num = binary_num[x] * 2 ** power  #this is the way that each number in the binary sequence gets converted by
  power += 1 
  x = x - 1  # I used this to try to change the character in the string, but this is where problems happened
print(decimal_num)

#couldnt get this code to work, but I felt like I was on the right track


#Question 2

print('Input a set of words with a ? instead of a space')
s = (input())
num = s.count('?')  # this counts number of space between words
print (s.replace('?', ' ')) # .replace command is used to put in spaces
print(('There are'),(num + 1),('words in the sentence')) # the + 1 is there to get the word count, as there is always once less space then there are words in a sentence.