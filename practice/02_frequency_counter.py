def count_character_frequencies(input_string):
    frequency_counter = {}
    for char in input_string:
        if char in frequency_counter:
            frequency_counter[char] += 1
        else:
            frequency_counter[char] = 1
    return frequency_counter


# Example usage:
if __name__ == "__main__":
    test_string = "hello world"
    frequencies = count_character_frequencies(test_string)
    print(frequencies)
# This will output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
# This function counts the frequency of each character in the input string.
