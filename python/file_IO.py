def process_file():
    try:
        # Ask user for input file name
        input_filename = input("Enter the name of the input file: ")
        
        # Try to open and read the file
        try:
            with open(input_filename, 'r') as input_file:
                content = input_file.read()
                
                # Modify the content (in this case, capitalize everything)
                modified_content = content.upper()
                
                # Create output filename by adding '_modified' before the extension
                output_filename = input_filename.rsplit('.', 1)
                output_filename = f"{output_filename[0]}_modified.{output_filename[1]}"
                
                # Write modified content to new file
                with open(output_filename, 'w') as output_file:
                    output_file.write(modified_content)
                    
                print(f"Successfully processed file. Modified content saved to: {output_filename}")
                
        except FileNotFoundError:
            print(f"Error: The file '{input_filename}' was not found.")
        except PermissionError:
            print(f"Error: Permission denied to access '{input_filename}'.")
        except UnicodeDecodeError:
            print(f"Error: Unable to read '{input_filename}'. The file might be binary or encoded differently.")
            
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    print("File Processing Program")
    print("----------------------")
    process_file()