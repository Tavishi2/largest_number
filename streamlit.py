import streamlit as st

def find_maximum(num1, num2, num3):
    """
    Function to find the maximum of three numbers.
    """
    return max(num1, num2, num3)

def main():
    """
    Main function to create the Streamlit app.
    """
    st.title("Maximum Number Finder App")
    st.write("Enter three numbers below:")

    # Create blank boxes for user input
    num1 = st.text_input("Enter the first number:")
    num2 = st.text_input("Enter the second number:")
    num3 = st.text_input("Enter the third number:")

    # Convert input to float (if valid)
    try:
        num1 = float(num1)
        num2 = float(num2)
        num3 = float(num3)
    except ValueError:
        st.error("Please enter valid numbers.")

    # Create button to find maximum
    if st.button("Find Maximum"):
        # Ensure all inputs are valid
        if num1 is not None and num2 is not None and num3 is not None:
            # Find the maximum number
            maximum = find_maximum(num1, num2, num3)
            # Display the maximum number
            st.success(f"The maximum number is: {maximum}")

if __name__ == "__main__":
    main()
