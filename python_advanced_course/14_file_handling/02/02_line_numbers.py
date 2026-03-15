from string import punctuation

with open("text.txt") as input_file, open("output.txt", "w") as output_file:
    result = []
    for row_idx, line in enumerate(input_file):
        letter_count = 0
        punctuation_count = 0

        for ch in line:
            if ch.isalpha():
                letter_count += 1
            elif ch in punctuation:
                punctuation_count += 1

        result.append(f"Line {row_idx + 1}: {line.strip()} ({letter_count})({punctuation_count})")

    output_file.write("\n".join(result))
