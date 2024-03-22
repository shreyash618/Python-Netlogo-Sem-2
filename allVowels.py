## Shreya Shukla
## Intro CS2 09
## HW 14: While All This Is Happening
## 2019--03--07

#reads a string and prints the vowels in the word.

word = str (input ("Enter a word:"))
vowels = ""
i = len (word)
while i > 0:
    i += -1
    if word [i] =="a" or word [i] == "e" or word [i] == "i" or word [i] == "o" or word [i] == "u":
        vowels = word [i] + vowels
if i == 0:
    if vowels == "":
        print ("This contains no vowels.")
    else:
        print (vowels)

## people should return eoe
## apple should return ae
## sky should return "This contains no vowels."
