import string

def is_pangram(s):
    # Convert the string to lowercase and remove non-alphabet characters
    s = ''.join(filter(str.isalpha, s.lower()))
    
    # Create a set of unique characters in the cleaned string
    unique_chars = set(s)
    
    # Check if the set of unique characters contains all alphabets
    return len(unique_chars) == 26  # There are 26 letters in the English alphabet

# Example usage:
sentence = "The quick brown fox jumps over the lazy dog"
result = is_pangram(sentence)
print(result)  # Output: True
