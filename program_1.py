#Logan H's Name Counter Program
#
# 1st: Define function to count names in the file
def count_names():
    """
    Reads a file named 'names.txt' and counts the number of names stored in it.
    """
    try:
        # 2nd: Open and read the file
        with open("names.txt", "r") as file:
            names = file.readlines()  # Read all lines into a list
            total_names = len(names)  # Count the number of lines

        # 3rd: Display the total count
        print(f"\nTotal number of names in the file: {total_names}")

    except FileNotFoundError:
        # 4th: Handle case where file is missing
        print("Error: The file 'names.txt' does not exist.")

# 5th: Run the function
count_names()
