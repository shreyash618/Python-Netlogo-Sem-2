# Shreya Shukla
# Intro CS2 pd 09
# HW #23 : searCHandFind
# 2019--03--19

def upTo (target, List):
    '''Assumes target is a string and List is a list.
    Return either an empty list or a list containing all the items that preceed the target'''
    if target in List:
        List = List [0 : len (List) - 1]
        upTo (target, List)
    else:
        print (List)
upTo (1, [2,3,1]) #should print [2, 3]
upTo ('hello', [2,3,1]) #should print [2, 3, 1]
upTo ('cat', ['cat', 'dog']) #should print []

def UPTO (TARGET, LIST):
    '''Assumes TARGET is a string and LIST is a list.
    Return either an empty list or a list containing all the items that preceed the target'''
    while TARGET in LIST:
        LIST = LIST [0 : len (LIST) - 1]
    if TARGET not in LIST:
        print (LIST)
UPTO (1, [2,3,1]) #should print [2, 3]
UPTO ('hello', [2,3,1]) #should print [2, 3, 1]
UPTO ('cat', ['cat', 'dog']) #should print []

def findR (ch, word):
    '''Assumes ch is a 1 character string and word is also a string.
    If ch is in word, returns the index of ch in word. Otherwise, it prints a statement saying ch is not in the word.'''
    if ch == word [len (word) -1]:
        print (len (word) - 1)
    elif len (word) - 1 != 0:
        word = word [0 : len (word) -1]
        findR (ch, word)
    else:
        print (ch + ' is not in the string')

findR ('1', '1234123') #should print 4
findR ('1', '21314') #should print 3
findR ('2', '21314') #should print 0
findR ('0', '1234123') #should print 0 is not in the string

def FindR (Ch, Word):
    '''Assumes Ch is a 1 character string and Word is also a string.
    If Ch is in Word, returns the index of Ch in Word. Otherwise, it prints a statement saying Ch is not in the word.'''
    while Ch != Word [len (Word) - 1]:
        if len (Word) - 1 != 0:
            Word = Word [0 : len (Word) -1]
        else:
            print (Ch + ' is not in the string')
            break
    if Ch == Word [len (Word) - 1]:
        print (len (Word) - 1)
FindR ('1', '1234123') #should print 4
FindR ('1', '21314') #should print 3
FindR ('2', '21314') #should print 0
FindR ('0', '1234123') #should print 0 is not in the string
