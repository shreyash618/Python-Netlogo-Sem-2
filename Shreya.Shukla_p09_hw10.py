# Shreya Shukla
# Intro CS2 pd09
# HW 10: LetsStringItAllTogether
# 2019--03--03

def strDemo (n) :
    print (len (n)) ## the length
    print n [0] ## the first character
    print n [len (n) - 1] ## the last character

    print n [(len (n) - 1) / 2] if len (n) %  2 == 1 else n [(len (n) - 1) / 2 : ((len (n) - 1) / 2) + 2] ## the middle character
    ## if n is even, there will be two middle characters, but if n is odd, there will be only one middle character

    if len (n) % 2 == 1: ## if n has a ODD number of characters
        print n [0: (len (n) / 2) + 1] ## the first half
        print n [(len (n) / 2): len (n)] ## the second half
        
    elif len (n) % 2 == 0: ## if n has a EVEN number of characters
        print n [0: len (n) / 2] ## the first half, w/ middle character
        print n [(len (n) / 2) : 2 * (len (n) / 2) ] ## the second half, w/ middle character

    print [n + n] ## repeats the string twice
    print ["aaa" + n + "zzz"] ## adds 'aaa' to the front of the string and 'zzz' to the end   

strDemo ("meow")
## 4
## m
## w
## e, o
## me
## ow
## meowmeow
## aaameowzzz
print ("\n")

strDemo ("cat")
## 3
## c
## t
## a
## ca
## at
## catcat
## aaacatzz
print ("\n")

strDemo ("kitten")
## 6 
## k
## n
## t,t
## kit
## ten
## kittenkitten
## aaakittenzzz
print ("\n")

strDemo ("Siamese")
## 7
## S
## e
## m
## Siam
## mese
## SiameseSiamese
## aaaSiamesezzz
print ("\n")

strDemo ("CatsAreCute")
## 11
## C
## e
## r
## CatsAr
## reCute
## CatsAreCuteCatsAreCute
## aaaCatsAreCutezzz
print ("\n")

strDemo ("SphynxCats")
## 10
## S
## s
## n, x
## Sphyn
## xCats
## SphynxCatsSphynxCats
## aaaSpyhnxCatszzz
