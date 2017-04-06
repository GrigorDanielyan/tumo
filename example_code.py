s = '"What\'s up guys" said Robert'

s1 = '"What\'s up guys" said Robert'
s2 = "'What\'s up guys' said Robert"
s3 = '\'What\'s up guys\' said Robert'
s4 = """\'What\'s up guys\' said Robert"""

print('\n',s1,'\n',s2,'\n',s3,'\n',s4)


days = ['Sun', 'Mon', 'Tue', 'Wed','Thur', 'Fri', 'Sat']
numbers = [1,2,3,4,5,6,7,8,9,10]
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

numbers = [1,2,3,4,5]
numbers_same = numbers
numbers_copy = numbers[:]
print(numbers_copy)

print(id(numbers_copy))
print(id(numbers))

link = 'http://www.main.com/smith/index.html'

events = '9/13 2:30 PM\n9/14 11:15 AM\n9/14 1:00 PM\n9/15 9:00 AM'

event = "Tuesday, Feb 29, 2012 -- 3:35 PM"

prod = 'bread'
cost = 2
wght = 700
total = cost*wght
print(prod, cost, wght, total)
#bread 2 700 1400
print(prod, cost, wght, total, sep=': ')
#bread: 2: 700: 1400
print(prod, cost, wght, total, sep=':::')
#bread:::2:::700:::1400

pets = ['boa', 'cat', 'dog']

day = 'Wednesday'
month = 'March'
weekday = 'Wednesday'
month = 'March'
day = 10
year = 2010
year = 2012
hour = 11
minute = 45
second = 33
print(hour+':'+minute+':'+second)


lst = ['Jeff Bezos','Tim Cook', 'Larry Ellison']


directory = r"C:\Users\Training\Desktop\python"

#---

The 3 lines in this file end with the new line character.

There is a blank line above this line.

#---

def numChars(filename):
    '''returns the number of characters in file   
    filename'''

    infile = open(filename, 'r')
    content = infile.read()
    infile.close()

    return len(content)

def numWords(filename):
    '''returns the number of words in file   
    filename'''

    infile = open(filename)
    content = infile.read()
    infile.close()
    wordList = content.split()

    return len(wordList)
    
def numWords(filename):
    '''returns the number of words in file   
    filename'''

    infile = open(filename)
    content = infile.read()
    infile.close()
    wordList = content.split()

    return len(wordList)

    
input = open("data.txt")
for line in input:
	print(line.strip()) 



