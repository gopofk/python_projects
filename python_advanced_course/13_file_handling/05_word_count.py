import re

# Read words
with open('words.txt', 'r') as words_file:
    words = words_file.read().lower().split()

# Read text
with open('text.txt', 'r') as text_file:
    text = text_file.read().lower()

word_counts = {}

for word in words:
    pattern = r'\b' + re.escape(word) + r'\b'
    matches = re.findall(pattern, text)
    word_counts[word] = len(matches)

# Sort by frequency (descending)
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Write results
with open('result.txt', 'w') as result_file:
    for word, count in sorted_words:
        result_file.write(f"{word} - {count}\n")
