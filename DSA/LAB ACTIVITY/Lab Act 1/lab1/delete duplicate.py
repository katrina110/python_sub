
# Function to remove duplicate characters from a string
def remove_duplicates(input_str):
    char_set = set()
    result = ""
    for char in input_str:
        if char not in char_set:
            char_set.add(char)
            result += char
    return result

# Input the number of strings
N = int(input("Enter the number of strings: "))

# Input and process each string
for _ in range(N):
    input_str = input("Enter a string: ")
    result_str = remove_duplicates(input_str)
    print(result_str)


