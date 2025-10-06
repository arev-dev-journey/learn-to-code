# exercises/day6_io_exceptions.py

def write_names_to_file(names, filename="files/names.txt"):
    """Writes a list of names to a file, each on a new line."""
    try:
        with open(filename, "w") as file:
            for name in names:
                file.write(name + "\n")
    except Exception as e:
        print(f"Error writing to file: {e}")

def read_names_from_file(filename="files/names.txt"):
    """Reads and prints the contents of a file, handling exceptions."""
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error reading file: {e}"

def count_words_in_file(filename="files/names.txt"):
    """Reads a file and counts the number of words in it."""
    try:
        with open(filename, "r") as file:
            content = file.read()
            return len(content.split())
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error reading file: {e}"

def safe_read_file(filename="files/names.txt"):
    """Safely opens and reads a file, returning 'File not found' if missing."""
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."

def safe_divide(a, b):
    """Divides two numbers and handles ZeroDivisionError."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."

if __name__ == "__main__":
    # Example function calls
    names = ["Alice", "Bob", "Charlie"]
    write_names_to_file(names)
    print(read_names_from_file())
    print(count_words_in_file())
    print(safe_read_file())
    print(safe_divide(10, 2))
