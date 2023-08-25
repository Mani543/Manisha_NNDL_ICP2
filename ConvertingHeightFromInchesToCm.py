# Converting inches to CM
def inches_to_cm(inches):
    return inches * 2.54
# Using Nested Interactive Loop
def convert_heights_nested_loop(heights_inches):
    heights_cm = []

    for height_inches in heights_inches:
        height_cm = inches_to_cm(height_inches)
        heights_cm.append(height_cm)  # Rounding to 2 decimal places

    return heights_cm

# Using List Comprehensions
def convert_heights_list_comprehension(heights_inches):
    heights_cm = [inches_to_cm(height) for height in heights_inches]
    return heights_cm

# Main method
def main():

    heights_inches = [float(height) for height in input("Enter heights (in inches) of customers separated by spaces: ").split()]

    # Converting the heights from inches to Centimeters Using Nested Interactive Loop
    heights_nested = convert_heights_nested_loop(heights_inches)
    print("Using Nested Interactive Loop:")
    print("Heights in Centimeters:", heights_nested)

    # Converting the heights from inches to Centimeters Using List Comprehensions
    heights_list_comp = convert_heights_list_comprehension(heights_inches)
    print("\nUsing List Comprehensions:")
    print("Heights in Centimeters:", heights_list_comp)

if __name__ == "__main__":
    main()
