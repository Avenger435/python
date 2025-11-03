class Solution:

    def __init__(self):
        pass

    def replace_caps_to_smalls(self, input_string):
        # Convert all uppercase letters to lowercase
        return input_string.lower()


if __name__ == "__main__":
    solution = Solution()
    input_string = "This is a String with Mixed CASE Letters."
    output_string = solution.replace_caps_to_smalls(input_string)
    print(output_string)  # Output: "this is a string with mixed case letters."
