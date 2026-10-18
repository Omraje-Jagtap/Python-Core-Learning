'''Question: Write a Python program to 
remove punctuation from a sentence using a function.'''

def remove_punctuation(text):
    result = ""
    punctuation = ".,!?;:'\"()[]{}-"

    for ch in text:
        if ch not in punctuation:
            result = result + ch

    return result


sentence = input("Enter a sentence: ")
print("Sentence without punctuation:", remove_punctuation(sentence))
