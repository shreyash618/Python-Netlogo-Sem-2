## Shreya Shukla
## Intro CS2 pd09
## HW 12: ASCII anything
## 2019--03--06

# reads in a string, assume all lowercase letters, then determines whether the string contains a vowel or not.

def hasAvowel (n) :
    y = len (n)
    function2 (y, n)


def function2 (y, n):
    if y > 0:
        if n [ y -1] == "a" or n [ y -1] == "e" or  n [ y -1] == "i" or  n [ y -1] == "o" or  n [ y -1] == "u":
            print ("The string contains a vowel.")
        else:
            y = y -1
            function2 (y, n)
    else:
        print ("This does not contains any vowels.")

hasAvowel ("mom")
hasAvowel ("mazeltov")
hasAvowel ("l")
hasAvowel ("try")
hasAvowel ("cryptography")
