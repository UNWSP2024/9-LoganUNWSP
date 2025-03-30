#Logan H's Average Numbers Program
#
# 1st: Define function to read numbers and calculate total
def calculate_total():
    """
    Reads integers from 'numbers.txt', calculates their total,
    and handles potential IOError and ValueError exceptions.
    """
    try:
        # 2nd: Open the file for reading
        with open("numbers.txt", "r") as file:
            total = 0  # Initialize total sum
            count = 0  # Track number of numbers

            # 3rd: Read and process each line
            for line in file:
                try:
                    num = int(line.strip())  # Convert line to integer
                    total += num
                    count += 1
                except ValueError:
                    print(f"Warning: Skipping invalid data '{line.strip()}' (not an integer).")

        # 4th: Display total if numbers were processed
        if count > 0:
            print(f"Total of all numbers: {total}")
        else:
            print("No valid numbers found in the file.")

    except IOError:
        print("Error: Could not read the file 'numbers.txt'. Ensure the file exists and is accessible.")


# 5th: Run the function
calculate_total()
