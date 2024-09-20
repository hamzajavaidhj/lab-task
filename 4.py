#  task 4

def luhn_check(card_number):
    digits = [int(d) for d in str(card_number)]
    digits.reverse()
    for x in range(1, len(digits), 2):
        digits[x] *= 2
        if digits[x] > 9:
            digits[x] -= 9
    total = sum(digits)
    return total % 10 == 0
card_number = 4532015112830366
print("Is the card number valid?",{luhn_check(card_number)})


def remove_punctuation(input_string):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    result = ""
    for a in input_string:
        if a not in punctuation:
            result += a
            print(result)
user_input = "Hello, I am Hamza...."
cleaned_string = remove_punctuation(user_input)
print(f"String without punctuation: {cleaned_string}")


def bubble_sort(words):
    a = len(words)
    for x in range(a):
        for y in range(0, a-x-1):
            if words[y] > words[y+1]:
                words[y], words[y+1] = words[y+1], words[y]
    return words
words_list = ["banana", "apple", "cherry", "date"]
sorted_words = bubble_sort(words_list)
print(f"Sorted words: {sorted_words}")

