class Solution:
    """
    A class containing methods for case conversion in strings.
    """

    def __init__(self):
        pass

    def replace_caps_to_smalls(self, input_string):
        """
        Convert all uppercase letters to lowercase in the input string.

        This method uses Python's built-in lower() method to convert
        all uppercase characters to their lowercase equivalents.

        Args:
            input_string (str): The input string to convert

        Returns:
            str: The converted string with all characters in lowercase

        Example:
            >>> solution = Solution()
            >>> solution.replace_caps_to_smalls("Hello World")
            'hello world'
        """
        # Convert all uppercase letters to lowercase
        return input_string.lower()


if __name__ == "__main__":
    solution = Solution()
    input_string = "This is a String with Mixed CASE Letters."
    output_string = solution.replace_caps_to_smalls(input_string)
    print(output_string)  # Output: "this is a string with mixed case letters."
