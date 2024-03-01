def find_missing_number(sequence):
    # Sort the sequence
    sequence.sort()
    
    # Check for the missing number
    for i in range(len(sequence) - 1):
        if sequence[i + 1] - sequence[i] != 1:
            missing_number = sequence[i] + 1
            return missing_number

    # If no missing number is found within the sequence
    return None

# Example usage:
sequence = [1, 2, 3, 5, 6, 7, 8]
missing_number = find_missing_number(sequence)
if missing_number:
    print("The missing number is:", missing_number)
else:
    print("No missing number found in the sequence.")
