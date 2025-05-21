def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("Reading file content:")
            for index, line in enumerate(file, start=1):
                print(f"Line {index}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function with the target filename
read_file("sample.txt")
