def generate_pascals_triangle(num_rows):
    triangle = []

    for i in range(num_rows):
        row = [1]  # First element in each row is always 1
        if triangle:
            last_row = triangle[-1]
            # Generating each element in the current row except the first and last
            row.extend([last_row[j] + last_row[j + 1] for j in range(len(last_row) - 1)])
            row.append(1)  # Last element in each row is always 1
        triangle.append(row)

    return triangle

def display_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(str(num) for num in row).center(60))

# Main program
num_rows = int(input("Enter the number of rows for Pascal's triangle: "))
pascals_triangle = generate_pascals_triangle(num_rows)
display_pascals_triangle(pascals_triangle)