#1 --Creating a program that reads a file and writes a modified version to a new file.
def read_and_modify_file(input_file, output_file):
    try:
        # Open the input file for reading
        with open(input_file, 'r') as file:
            content = file.readlines()

        # Modify the content as needed
        modified_content = []
        for line in content:
            # Example modification: Convert all text to uppercase
            modified_line = line.upper()
            modified_content.append(modified_line)

        # Open the output file for writing
        with open(output_file, 'w') as file:
            file.writelines(modified_content)

        print(f"File '{input_file}' has been successfully modified and saved as '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = 'input.txt'
output_file = 'output.txt'
read_and_modify_file(input_file, output_file)



#2 --Asking the user for a filename and handle errors if it doesn’t exist or can’t be read.
def read_and_modify_file():
    # Ask the user for the input filename
    input_file = input("Please enter the name of the file to read: ")

    try:
        # Open the input file for reading
        with open(input_file, 'r') as file:
            content = file.readlines()

        # Modify the content as needed
        modified_content = []
        for line in content:
            # Example modification: Convert all text to uppercase
            modified_line = line.upper()
            modified_content.append(modified_line)

        # Ask the user for the output filename
        output_file = input("Please enter the name of the file to save the modified content: ")

        # Open the output file for writing
        with open(output_file, 'w') as file:
            file.writelines(modified_content)

        print(f"File '{input_file}' has been successfully modified and saved as '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_file}' cannot be read.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
read_and_modify_file()
