# Shreya Shukla
# Intro CS2 period 9
# Labwork01 - Two Faced
# 2019--02--06

# face 1
hair1 = '\t' + '|' * 16
eyes1 = '\t|' + ' ' * 3 + 'o' + ' ' * 6 + 'o' + ' ' * 3 + '|'
ears1 = ' ' * 7 +  '_|' + ' ' * 14 + '|_'
ears1 = ears1 + '\n' + ' ' * 6 + '|_' + ' ' * 16 + '_|'
ears1 = ears1 + '\n\t' + '|' + ' ' * 14 + '|'
mouth1 = '\t|' +  ' ' * 3 + '|' + '_' * 6 + '|' + ' ' * 3 + '|'
chin1 =  '\t|' + '_' * 5 + ' ' * 4 + '_' * 5 + '|'
neck1 = '\t' + ' ' * 5 + '|' + ' ' * 4 + '|'

# face 1
print ("face 1")
print (hair1)
print (eyes1)
print (ears1)
print (mouth1)
print (chin1) 
print (neck1)


# face 2
hat = " " * 6 + "_" * 9 + " " * 7
hat = hat + '\n' + " " * 5 + "/" +  " " * 9 + "\ " + " " * 5 ## creates a trapeziodal hat
hair =  '  '+ '%' * 18 ##hair
forehead = "  !    _        ^  !  " ##creates eyebrows for the face
eyes = "  !    *        *  !  " ##eyes
nose = " C" + " " * 9 + ")" + " " * 8 + "D " ##creates a nose and two ears
gap = "  !" + " " * 16 + "!  "  ## this creates space between the nose and the mouth on the character's face
mouth = "  !       \_/      !  " ##mouth
chin = "   \::::::::::::::/  " ##creates a beard on character's face
chin = chin + '\n' + " " * 4 + "\::::::::::::/" ##extends the beard to one level down
neck = '\t' + "!    !"
neck = neck + '\n' + neck ##creates a neck for the character using exclamation points


#face 2
print ("face 2")
print (hat)
print (hair)
print (forehead)
print (eyes)
print (nose)
print (gap)
print (mouth)
print (chin)
print (neck)
