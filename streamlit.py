def find_maximum(a, b, c):
    """
    Function to find the maximum of three numbers.
    """
    return max(a, b, c)

def main():
    """
    Main function to take inputs from the user and find the maximum.
    """
    print("Welcome to the Maximum Number Finder App!")
    print("Please enter three numbers.")

    # Take input from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))

        # Find the maximum number
        maximum = find_maximum(num1, num2, num3)

        # Print the maximum number
        print("The maximum number is:", maximum)

    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
