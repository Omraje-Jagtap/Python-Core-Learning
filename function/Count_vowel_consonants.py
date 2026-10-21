'''Question: Write a Python program to count the number 
of vowels and consonants in a string using a function.'''

def count_letters(text):
    vowels = 0
    consonants = 0

    for ch in text.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants


text = input("Enter a string: ")

vowels, consonants = count_letters(text)

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
