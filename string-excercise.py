s = "Hello, World!"
print(s.upper())  # Convert to uppercase
print(s.lower())  # Convert to lowercase
print(s.replace("World", "Python"))  # Replace substring
print(s.split(", "))  # Split string into a list
print(s.find("World"))  # Find substring index
print(s.startswith("Hello"))  # Check if string starts with a substring
print(s.endswith("!"))  # Check if string ends with a substring
print(s.strip("!"))  # Remove specific characters from both ends
print(s.center(20, "-"))  # Center the string with padding
print(s.count("o"))  # Count occurrences of a substring
print(s.isalpha())  # Check if all characters are alphabetic
print(s.isdigit())  # Check if all characters are digits
# Join a list of strings with the original string as a separator
print(s.join(["Hello", "Python"]))
print(s.title())  # Convert to title case
print(s[::-1])  # Reverse the string
print(s.encode("utf-8"))  # Encode the string to bytes
# Decode bytes back to string, ignoring errors
# print(s.encode("utf-8").decode("utf-8", "ignore"))
