import re


class Solution:
    def remove_special_characters(self, input_string):
        # Use regex to remove special characters, keeping only alphanumeric and spaces
        cleaned_string = re.sub(r'[^a-zA-Z0-9\s]', '', input_string)
        return cleaned_string

    def remove_special_chars(self, input_string):
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
