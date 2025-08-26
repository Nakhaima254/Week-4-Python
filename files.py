# file = open('newFile.pdf' , 'w')
# file.write("Hello world,\n")

def file_read_write():
    # Ask user for input filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Try opening and reading the file
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Create a new output file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f" Modified file has been saved as: {new_filename}")

    except FileNotFoundError:
        print(" Error: The file was not found. Please check the filename and try again.")
    except PermissionError:
        print(" Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")


# Run the function
file_read_write()
# This script reads a file, modifies its content, and writes it to a new file.