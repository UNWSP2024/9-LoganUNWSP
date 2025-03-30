#Logan H's Random Number File Writer
#
# 1st: Import the random module
import random


# 2nd: Define function to generate and write random numbers
def write_random_numbers():
    """
    Writes a user-defined number of random numbers (1-500) to 'random_numbers.txt'.
    Max limit: 1000 numbers.
    """
    # 3rd: Prompt user for the number of random numbers
    try:
        count = int(input("Enter the number of random numbers to generate (1-1000): "))

        # 4th: Validate the input range
        if count < 1 or count > 1000:
            print("Error: Please enter a number between 1 and 1000.")
            return

        # 5th: Open file for writing
        with open("random_numbers.txt", "w") as file:
            for _ in range(count):
                num = random.randint(1, 500)  # Generate random number (1-500)
                file.write(str(num) + "\n")  # Write to file

        # 6th: Confirm completion
        print(f"Successfully wrote {count} random numbers to 'random_numbers.txt'.")

    except ValueError:
        print("Error: Please enter a valid integer.")


# 7th: Run the function
write_random_numbers()
