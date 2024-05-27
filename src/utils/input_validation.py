# /src/utils/input_validation.py

# This validates non-zero user input and is generalized to accept float or int arguments.

# Dependencies: Import sys to enable exiting the program
import sys


# Function to validate non-zero user input, generalized for float or int input values
def validate_positive_num_account_input(user_value_in):
    """
    This function validates if the input is 0 or larger.  
    
    It uses isinstance() to identify the object's type and validates the input
    based on that object's type, or exits the application. I Used isinstance() 
    and not isdigit() as I was exploring ways to generalize the calling input 
    and test for int, float, or non-number string, but could only find built-in 
    methods to evaluate int or float, but not string.

    Args:
        user_value_in (float or int) : The user's input value

    Returns:
        Returns the validated and unchanged type casted value if a positive number.
        If it is a negitive number, the system lets the user know what value is 
        expected as input and exists the program.
    """
    if isinstance(user_value_in, float):
        if user_value_in >= 0.0:
            user_value = user_value_in
            return user_value
        else:
            print(f"Please restart the program and enter a number zero or larger. You entered {user_value_in}")
            sys.exit("Exiting")
    else:
        if user_value_in >= 0:
            user_value = user_value_in
            return user_value
        else:
            print(f"Please restart the program and enter a number zero or larger. You entered {user_value_in}")
            sys.exit("Exiting")


def main():
    """
    Test the valiadtion functionality.
    
    Mock Args:
        Test 1 - user_input_in (int) : 10
        Test 2 - user_input_in (float) : 10.0
        Test 3 - user_input_in (int) : -10

    Results:
        Test 1 - success message
        Test 2 - success message
        Test 3 - system exit message handled in validation 
    """
    # Test int
    user_input_in = "10"
    print(f"user input is {user_input_in}")
    user_input_int = int(user_input_in)
    user_input_certified = validate_positive_num_account_input(user_input_int)
    print(f"Pass. Certified 'int'. Entered: {user_input_certified}")

    # Test float
    user_input_in = "10.0"
    print(f"user input is {user_input_in}")
    user_input_int = float(user_input_in)
    user_input_certified = validate_positive_num_account_input(user_input_int)
    print(f"Pass. Certified 'float'. Entered: {user_input_certified}")

    # Test negitive number
    user_input_in = "-10"
    print(f"user input is {user_input_in}")
    user_input_int = int(user_input_in)
    user_input_certified = validate_positive_num_account_input(user_input_int)
    print("Fail. The system should have quit and you should not have seen this message.")


if __name__ == "__main__":
    main()
    






