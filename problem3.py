def is_palindrome(word):
    return word == word[::-1]

def convert_to_palindromes(sentence):
    words = sentence.split()
    result = []

    for word in words:
        if not is_palindrome(word):
            palindrome_word = word + word[::-1]
            result.append(palindrome_word)
        else:
            result.append(word)

    return ' '.join(result)

# Example usage:
user_sentence = input("Enter a sentence: ")
output_sentence = convert_to_palindromes(user_sentence)
print("Output:", output_sentence)

