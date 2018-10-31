# Function Practice Exercises
#
# Problems are arranged in increasing difficulty:
#
# Warmup - these can be solved using basic comparisons and methods
# Level 1 - these may involve if/then conditional statements and simple methods
# Level 2 - these may require iterating over sequences, usually with some kind of loop
# Challenging - these will take some creativity to solve

# WARMUP SECTION:
# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd
#
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

#These are my solutions to the given functions below

def lesser_of_two_evens(a,b):
    #check to see if and and b are even
    if(a%2 == 0 and b%2 == 0):
        #both are even and a is less than b
        if(a < b):
            return a
        else:
        #both are even and b is less than ba
            return b
    #either a or b is odd
    else:
        #return the larger number
        if(a > b):
            return a
        else:
            return b


print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))
print(lesser_of_two_evens(7,5))
print(lesser_of_two_evens(5,7))
print(lesser_of_two_evens(20,18))
print("\n")


# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(s):
    #split string on space and assign to a variable. it returns a list
    a = s.split(" ")

    b = "" #empty string

    #need to iterate through the list and pull the first letter from each word. Attach it to empty string
    for word in a:
        b += word[0]

    #return in the substring going forward is the same going backward. if all of the letter are the same then return true
    return b[0:] == b[::-1]


print(animal_crackers("Levelheaded Llama"))
print(animal_crackers("Crazy Kangaroo"))
print("\n")


# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
# If not, return False
#
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

def makes_twenty(x,y):
    return (x == 20 or y == 20 or (x+y == 20))

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))
print("\n")



# LEVEL 1 PROBLEMS
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
#
# old_macdonald('macdonald') --> MacDonald
#
# Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(name):
    #since we know te exact postions we need to capitalize, we can just use slicing
    first_letter = name[0]
    letters_between_zero_and_four = name[1:3]
    fourth_leter = name[3]
    letters_between_four_and_end_of_string = name[4:]


    return first_letter.upper() + letters_between_zero_and_four + fourth_leter.upper() + letters_between_four_and_end_of_string



print(old_macdonald("macdonald"))
print("\n")


# MASTER YODA: Given a sentence, return a sentence with the words reversed
#
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'
#
# Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:
#
# >>> "--".join(['a','b','c'])
# >>> 'a--b--c'
#
# This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:
#
# >>> " ".join(['Hello','world'])
# >>> "Hello world"

def master_yoda(text):
    #let's use the split method to return a list of strings that were separated by a space
    working_string = text.split(" ")

    reversed(working_string)

    b = " ".join(reversed(working_string))

    return b


print(master_yoda("I am home"))
print(master_yoda('We are ready'))
print("\n")



# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
#
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
#
# NOTE: abs(num) returns the absolute value of a number

def almost_there(n):
    return (n>=90 and n<=110) or (n>=190 and n<=210)



print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
print("\n")


# LEVEL 2 PROBLEMS
# FIND 33:
#
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(nums):
    for value in range(0, len(nums)-1): #iterate until the second to last entry in the list
        #checking the values are the current index and the next index to see if they are 3
        if(nums[value] == 3 and nums[value+1] == 3):
            return True
        else:
            continue #if values aren't both 3, then continue to the next loop iteration

    return False #if after the loop is done, we haven't found concurrent 3's, so we return False



print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
print("\n")


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
#
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(s):
    working_string = ""

    #iterate through the string and use *3 and concatenate to the working_string
    for letter in s:
        working_string += 3*letter

    return working_string


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))
print("\n")


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
#
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

def blackjack(a,b,c):
    #check to see if sum of a,b,c is greater than 21. Also, need to check if you can an Ace(11) an need to decrease sum by 10
    if ( (a+b+c) > 21 and  ( (a == 11) or (b == 11) or (c ==11) ) ):
        return (a+b+c-10)
    elif((a+b+c) > 21):
        return "Bust"
    else:
        return a+b+c


print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))
print("\n")
