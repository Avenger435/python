# Determine voting eligibility based on age
"""
    This program checks if a person is eligible to vote based on their age.
"""
age = 12
if age >= 18:
    message = "You are eligible to vote."
else:
    message = "You are not eligible to vote."

print(message)

print(id(message))
