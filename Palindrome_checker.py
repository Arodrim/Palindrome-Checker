import string

print("Palindrome_Checker_v1")
print("Welcome to the Palindrome Checker!")

while True:

    palindrome = input("Enter word or phrase:")

    lowercase = palindrome.lower()

    processed_text = lowercase.replace(" ", "")

    translator = str.maketrans("", "", string.punctuation)

    translated_text = processed_text.translate(translator)

    reversed_phrase = translated_text[::-1]
    print(reversed_phrase)

    if(reversed_phrase == translated_text):
        print("Yes!!, it's a palindrome")
    else:
        print("Nope, this isn't a palindrome")