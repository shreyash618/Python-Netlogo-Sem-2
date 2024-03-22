# Shreya Shukla
# IntroCS2 pd09
# 2019--05--14
# HW 40: WhenIsJune? Alphabetically?

# I have no idea what we learned in class, I was absent yesterday and I still have to get notes.
# So if I did something wrong, please note that it's not my fault.

months  = {'jan': 1, 'feb': 2, 'march':3, 'april':4, 'may':5, 'june':6,'july':7,
           'aug':8, 'sept':9, 'oct':10, 'nov':11, 'dec':12}
months2 = {'april':4, 'aug ':8, 'dec':12, 'feb':2, 'jan':1, 'july':7, 'june':6, 'march': 3, 'may': 5, 
            'nov':11,'oct':10,'sept':9}
def allMonths():
    '''Lists all the months and their numbers alphabetically.'''
    for i in months2:
        print (i, ':', months2[i])
allMonths()

def oddMonths():
    '''Lists all odd numbered months.'''
    for i in months:
        if months [i] % 2 == 1:
            print (i, end = ' ')

oddMonths()
