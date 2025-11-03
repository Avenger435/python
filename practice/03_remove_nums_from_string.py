input_string = "Th1s 1s a t3st str1ng w1th numb3rs 12345."
output_string = ''.join([char for char in input_string if not char.isdigit()])
print(output_string)  # Output: "Ths s a tst strng wth numbrs ."
