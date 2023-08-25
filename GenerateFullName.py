# Function to return alternative characters from a given string
def string_alternative(input_string):
    return input_string[::2]
# Main function
def main():
    # Prompting the user to enter a first name and a last name
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    # Concatenating the first and last names
    full_name = first_name + " " + last_name
    # Print the full name
    print("Full name:", full_name)
    # Calling the string_alternative() function
    alternate_chars = string_alternative(full_name)
    # Displaying the alternate characters in the given full name
    print("Alternate characters in the given full name are as follows:", alternate_chars)

if __name__ == "__main__":
    main()