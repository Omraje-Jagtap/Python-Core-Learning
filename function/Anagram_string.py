'''Question: Write a Python program to check whether 
   two strings are anagrams using a function.'''

def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)


a = input("Enter first string: ")
b = input("Enter second string: ")

print("Anagrams" if is_anagram(a, b) else "Not anagrams")
