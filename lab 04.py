#TASK 01
#LUHN ALGORITHM:

def luhn_algorithm(card_number):
    # Reverse the card number and convert it to a list of integers
    card_digits = [int(digit) for digit in str(card_number)][::-1]
    
    total_sum = 0

    # Process each digit
    for i, digit in enumerate(card_digits):
        if i % 2 == 1:  # Double every second digit
            digit *= 2
            if digit > 9:  # Subtract 9 from numbers greater than 9
                digit -= 9
        total_sum += digit

    # If total_sum modulo 10 is 0, the card number is valid
    return total_sum % 10 == 0

# Example:
card_number = input("Enter your card number: ")
if luhn_algorithm(card_number):
    print("Card is valid!")
else:
    print("Card is invalid.")


#TASK 02
#Removes punctuation from a string without using the remove() function


def remove_punctuation(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    result = ""

    # Build the result string by skipping punctuation characters
    for char in text:
        if char not in punctuations:
            result += char
    return result

# Example:
user_input = input("Enter a string: ")
cleaned_string = remove_punctuation(user_input)
print("String without punctuations:", cleaned_string)



#TASK 03
# Sorts words in alphabetical order without using the built-in sort() function.


def bubble_sort(words):
    n = len(words)
    for i in range(n):
        for j in range(0, n - i - 1):
            if words[j] > words[j + 1]:
                # Swap if the word is greater (alphabetically)
                words[j], words[j + 1] = words[j + 1], words[j]
    return words

# Example:
user_input = input("Enter a string: ")
words = user_input.split()
sorted_words = bubble_sort(words)
print("Words in alphabetical order:", ' '.join(sorted_words))

