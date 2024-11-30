def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")
        return None

def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"File '{filename}' has been written successfully.")
    except IOError:
        print(f"Error: Could not write to the file '{filename}'.")

def modify_content(content):
    # Example modification: Convert all text to uppercase
    return content.upper()

def main():
    input_filename = input("Enter the name of the file to read: ")
    content = read_file(input_filename)
    
    if content:
        modified_content = modify_content(content)
        output_filename = input("Enter the name of the file to write the modified content to: ")
        write_file(output_filename, modified_content)

if __name__ == "__main__":
    main()
