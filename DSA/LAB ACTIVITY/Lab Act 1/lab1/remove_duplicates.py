
# Function to remove duplicate characters from a string
def remove_duplicates(input_str):
    result = ""
    seen = set()
    duplicate = set()

    for char in input_str:
        if char not in seen and char != ' ':
            seen.add(char)
        # Add in duplicate
        elif char in seen:
            duplicate.add(char)

        # Refining the results
    for char in seen:
        if char not in duplicate:
            result += char

    return result

# Input the number of strings
N = int(input("Indicate the number of strings: "))

# Input and process each string
print("Type your strings")
strings = []
for _ in range(N):
    string = input()
    strings.append(string.lower())

for string in strings:
    modified_string = remove_duplicates(string)
    print(modified_string)
