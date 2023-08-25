# function to return word_counts array after counting words in each line and storing them in word_counts array
def count_words(line, word_counts):
    words = line.split()
    # loop to count the occurance of each word
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts
# Main function
def main():
    input_filename = "input.txt"
    output_filename = "output.txt"

    try:
        # Reads the input file
        with open(input_filename, 'r') as input_file:
            readline = input_file.readlines()

        word_counts = {}
        for line in readline:
            line = line.strip()  # Remove leading/trailing whitespace
            # Function to count words
            word_count = count_words(line, word_counts)
        # Writing the input file lines to output file
        with open(output_filename, 'w') as output_file:
            for line in readline:
                output_file.write(line)

            output_file.write("\nWord_Count:\n")
            # Displaying the words and its count in output file
            for word, count in word_counts.items():
                output_file.write(f"{word}: {count}\n")
                print(f"{word}: {count}")

    except FileNotFoundError:
        print(f"File '{input_filename}' not found.")

if __name__ == "__main__":
    main()
