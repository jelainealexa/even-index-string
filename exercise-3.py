# Print characters from a string that are present at an even index number

# Enter a string
input_string = input("Enter a string: ")

# Declare the word variable
string = input_string

# Print original string and even index characters
print(f"Original string is {string}")
print("Printing only even index characters")

# Iterate each character of the string

# Start: 1
# Stop: length of the word
# Step: 2
for i in range(1, len(string), 2):
    # Print characters at the even index number
    print(string[i])