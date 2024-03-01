# 1.Create a function that counts the occurrences of each character in a string.
#Chat-Gpt😭
def count_characters(string):
    """Count the occurrences of each character in a string."""
    char_count = {}
    for char in string:
        print(char_count) #to check the how the char count is working
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print(char_count)
    return char_count

# Example usage:
input_string = input("Enter a string: ")
character_counts = count_characters(input_string)
print(character_counts)
print("Occurrences of each character:")
for char, count in character_counts.items():
    print(f"'{char}': {count}")