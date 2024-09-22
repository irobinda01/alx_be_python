size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Draw the pattern using a while loop
while row < size:
    # Use a for loop to print asterisks in the same row
    for _ in range(size):
        print("*", end="")
    # Move to the next line after completing a row
    print()
    # Increment the row counter
    row += 1
