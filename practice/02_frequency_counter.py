class Solution:
    """
    A class containing methods for counting character frequencies in strings.
    """

    def count_character_frequencies(self, input_string):
        """
        Count the frequency of each character in the input string.

        This method creates a dictionary where keys are characters and values
        are their occurrence counts in the input string.

        Args:
            input_string (str): The input string to analyze

        Returns:
            dict: A dictionary with characters as keys and their frequencies as values

        Example:
            >>> solution = Solution()
            >>> solution.count_character_frequencies("hello world")
            {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
        """
        frequency_counter = {}
        for char in input_string:
            if char in frequency_counter:
                frequency_counter[char] += 1
            else:
                frequency_counter[char] = 1
        return frequency_counter


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    test_string = "hello world"
    frequencies = solution.count_character_frequencies(test_string)
    print(frequencies)
# This will output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
# This function counts the frequency of each character in the input string.
