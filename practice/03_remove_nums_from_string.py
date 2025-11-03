class Solution:
    def __init__(self):
        pass

    """Remove all numeric digits from the input string."""

    def remove_numbers(self, input_string):
        # Iterate through each character and build a new string without digits
        return ''.join([char for char in input_string if not char.isdigit()])


if __name__ == "__main__":
    input_string = "Th1s 1s a t3st str1ng w1th numb3rs 12345."
    solution = Solution()
    output_string = solution.remove_numbers(input_string)
    print(output_string)  # Output: "Ths s a tst strng wth numbrs ."
