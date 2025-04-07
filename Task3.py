def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the contents of the file
            text = file.read()
            # Split the text into words using whitespace and count the length of the resulting list
            word_count = len(text.split())
            print(f"The number of words in the file is: {word_count}")
    except FileNotFoundError:
        print("The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'example.txt' with the path to your text file
count_words_in_file('example.txt')