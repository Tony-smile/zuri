# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

import string
all_punctuation = string.punctuation
# print(all_punctuation)

def find_anagram(word, anagram):
    # [assignment] Add your code here

    #remove trailing space and punctuation and convert it to lower case
    
    for pun in all_punctuation:
        word = word.replace(pun, '').replace(" ", "").lower()
        anagram = anagram.replace(pun, '').replace(" ", "").lower()
        #check if the length of the word is equal to the anagram

    if(len(word) == len(anagram)):
        #if equal sort them in ahz order
        sorted_word = sorted(word)
        sorted_anagram = sorted(anagram)

        #check if the character in both sorted_word and sorted_anagram is the same
        if(sorted_word == sorted_anagram):

            #if they are the same, that is, both words are gotten from the same alphabet combination return true (they're anagrams)
            return True
        else:
            return False


            #if length not equal, return false
    else:
        return False        

print(find_anagram(" Dormitory.", "Dirty Room."))