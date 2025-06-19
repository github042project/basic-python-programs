# string_analyzer.py
def analyze_string(s):
    vowels = "aeiouAEIOU"
    count_vowels = sum(1 for char in s if char in vowels)
    count_digits = sum(1 for char in s if char.isdigit())
    count_upper = sum(1 for char in s if char.isupper())

    print("Vowels:", count_vowels)
    print("Digits:", count_digits)
    print("Uppercase letters:", count_upper)

text = input("Enter a string: ")
analyze_string(text)

