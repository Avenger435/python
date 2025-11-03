class Solution:
    def replace_chars_with_ASCII(self, input_string: str) -> str:
        output_list = []
        for char in input_string:
            output_list.append(str(ord(char)))
        return " ".join(output_list)


# Example usage
if __name__ == "__main__":
    solution = Solution()
    input_string = "Th1s 1s a t3st str1ng w1th numb3rs 12345."
    output_string = solution.replace_chars_with_ASCII(input_string)
    print(output_string)
    # Output: "84 104 49 115 32 49 115 32 97 32 116 51 115 116 32 115 116 114 49 110 103 32 119 49 116 104 32 110 117 109 98 51 114 115
    # 32 49 50 51 52 53 ."
