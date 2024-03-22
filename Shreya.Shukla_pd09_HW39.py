# Shreya Shukla
# Intro CS pd09
# HW 39: Sets Formatted
# 2019--05--09

def makeset (a, b):
    '''Takes in two integers, a and b.
Returns a set of either a and b, if a is not equal to b, or just a.'''
    start, end= '{', '}'
    if a == b:
        print ('{}{}{}'.format(start,a,end))
    else:
        print('{}{},{}{}'.format(start,a, b,end))
makeset (2, 3)
# should return {2, 3}
makeset (3, 3)
# should return {3}
makeset (0 , False)
# should return {0}
