class Solution:
    """
    A class containing methods for removing numeric digits from strings.
    """

    def __init__(self):
        pass

    def remove_numbers(self, input_string):
        """
        Remove all numeric digits from the input string.

        This method iterates through each character and builds a new string
        containing only non-numeric characters.

        Args:
            input_string (str): The input string to clean

        Returns:
            str: The cleaned string with all numeric digits removed

        Example:
            >>> solution = Solution()
            >>> solution.remove_numbers("Th1s 1s a t3st str1ng")
            'Ths s a tst strng'
        """
        # Iterate through each character and build a new string without digits
        return ''.join([char for char in input_string if not char.isdigit()])


if __name__ == "__main__":
    input_string = "Th1s 1s a t3st str1ng w1th numb3rs 12345."
    solution = Solution()
    output_string = solution.remove_numbers(input_string)
    print(output_string)  # Output: "Ths s a tst strng wth numbrs ."
