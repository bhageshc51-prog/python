def palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return palindrome(word[1:-1])

text = input("Enter a word: ")

if palindrome(text):
    print("Palindrome")
else:
    print("Not a Palindrome")