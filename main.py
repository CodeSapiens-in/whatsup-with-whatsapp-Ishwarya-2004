import re
from collections import Counter

def most_used_words(file_path, num_words):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

        # Tokenize words
        words = re.findall(r'\b\w+\b', data.lower())

        # Count word frequencies
        word_counter = Counter(words)

        # Get the most common words
        most_common_words = word_counter.most_common(num_words)

        return most_common_words

# Usage example
file_path = '_chat.txt'  # Replace with the actual file path
num_words = 10  # Change this to get a different number of most common words
common_words = most_used_words(file_path, num_words)

print(f'The {num_words} most common words are:')
for word, count in common_words:
    print(f'{word}: {count} times')


    