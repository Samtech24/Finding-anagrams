# Check if two words are anagrams 
# Example:
# find_anagram("hello", "check") --> False
# find_anagram("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    str1= word.lower()
    str2= anagram.lower()

    if (len(str1)  == len(str2)):
        sorted_str1=sorted(str1)
        sorted_str2=sorted(str2)

        if(sorted_str1 == sorted_str2):
            print(True)
        else: print(False)

    else: print(False)

find_anagram("hello", "check")
find_anagram("below", "elbow")

