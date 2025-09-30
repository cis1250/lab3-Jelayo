import re

def is_sentence(text):
    if not isinstance(text, str) or not text.strip():
        return False

    if not text[0].isupper():
        return False

    if not re.search(r'[.!?]$', text):
        return False

    if not re.search(r'\w+', text):
        return False

    return True

user_sentence = input("Enter a sentence: ")

while (is_sentence(user_sentence) == False):
    print("This does not meet the criteria for a sentence.")
    user_sentence = input("Enter a sentence: ")
    
if (is_sentence(user_sentence) == True):
    user_sentence = user_sentence.replace(",", "")
    user_sentence = user_sentence.replace(".", "")
    divided = user_sentence.lower().split()

    for y in divided:
        print(y.title(), divided.count(y))

