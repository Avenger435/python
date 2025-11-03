input_string = "Hello World!"

output_list = []
for char in input_string:
    output_list.append(str(ord(char)))
# Output: "72 101 108 108 111 32 87 111 114 108 100 33"
print(" ".join(output_list))

# The code iterates through each character in the input string,
# converts it to its ASCII code using the ord() function,
# and joins the ASCII codes into a single string separated by spaces.
# Finally, it prints the resulting string of ASCII codes.
# Example usage:
# Input: "Th1s 1s a t3st str1ng w1th numb3rs 12345."
# Output: "84 104 49 115 32 49 115 32 97 32 116 51 115 116 32 115 116 114 49 110 103 32 119 49 116 104 32 110 117 109 98 51 114 115
# 32 49 50 51 52 53 ."
