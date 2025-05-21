def write_and_append_file(filename):
    try:
        # Step 1: Take user input and write to the file
        user_input = input("Enter text to write to the file: ")
        with open(filename, 'w') as file:
            file.write(f"{user_input}\n")
            print(f"Data successfully written to {filename}.")
            
        # Step 2: Append additional data
        additional_data = input("\nEnter additional text to append: ")
        with open(filename, 'a') as file:
            file.write(f"{additional_data}\n")
            print(f"Data successfully appended.")
            
        # Step 3: Read and display the final content
        print(f"\nFinal content of {filename}:")
        with open(filename, 'r') as file:
            for line in file:
                print(f"{line.strip()}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
write_and_append_file("output.txt")
