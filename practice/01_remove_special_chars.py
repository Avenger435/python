import re


class Solution:
    """
    A class containing different methods for removing special characters from strings.
    """

    def remove_special_characters(self, input_string):
        """
        Remove special characters from a string using regular expressions.

        This method uses regex to remove all characters that are not alphanumeric
        or whitespace, keeping only letters, numbers, and spaces.

        Args:
            input_string (str): The input string to clean

        Returns:
            str: The cleaned string with special characters removed

        Example:
            >>> solution = Solution()
            >>> solution.remove_special_characters("Hello, World!")
            'Hello World'
        """
        # Use regex to remove special characters, keeping only alphanumeric and spaces
        cleaned_string = re.sub(r'[^a-zA-Z0-9\s]', '', input_string)
        return cleaned_string

    def remove_special_chars(self, input_string):
        """
        Remove special characters from a string using iterative approach.

        This method iterates through each character and removes those that are
        neither alphanumeric nor whitespace. Note: This approach is less efficient
        than the regex method for large strings.

        Args:
            input_string (str): The input string to clean

        Returns:
            str: The cleaned string with special characters removed

        Example:
            >>> solution = Solution()
            >>> solution.remove_special_chars("Hello, World!")
            'Hello World'
        """
        for char in input_string:
            if not char.isalnum() and not char.isspace():
                input_string = input_string.replace(char, '')
        return input_string


# Example usage
if __name__ == "__main__":
    solution = Solution()
    test_string = "Hello, World! This is a test-string with special #characters$."

    # Using regex method
    result = solution.remove_special_characters(test_string)
    # Output: "Hello World This is a teststring with special characters"
    print(result)

    # Using iterative method
    result = solution.remove_special_chars(test_string)
    # Output: "Hello World This is a teststring with special characters"
    print(result)
