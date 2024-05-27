# src/customer_banking.py

# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
#
# Dependencies
from accounts.savings_account import create_savings_account
from accounts.cd_account import create_cd_account

from utils.input_validation import validate_positive_num_account_input # for input validation


# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, its interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.

    Inputs:
        User input that is stipped of spaces at the ends, type casted, and validated:
            savings_balance (float) : example data = 1000
            savings_interest (float) : example data = 5
            savings_maturity (int) : example data = 6

            cd_balance (float) : example data = 2000
            cd_interest (float) : example data = 4
            cd_maturity (float) :  example data = 12
    
    Outputs:
        prints to terminal:
            interest_earned (string) : formatted with commas every thousand and to 2 decimal places. 
                example data = 25.00
            updated_savings_balance (string) : formatted with commas every thousand and to 2 decimal places. 
                example data = 1,025.00
            updated_cd_balance (string) : formatted with commas every thousand and to 2 decimal places.
                example data = 2,080.00
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    # Removed leading and trailing spaces
    # Type casting the user input
    # Valiadting that the value is non-negitive.
    # In the future, ui can be enhanced
    savings_balance_in = float(input("Initial Saving's Balance: ").strip())
    savings_balance = validate_positive_num_account_input(savings_balance_in)
    
    savings_interest_in = float(input("Interest Rate: ").strip())
    savings_interest = validate_positive_num_account_input(savings_interest_in)

    savings_maturity_in = int(input("Number of months for the Savings Account: ").strip())
    savings_maturity = validate_positive_num_account_input(savings_maturity_in)

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    # The print statements 
    # In the future, ui can be enhanced 
    def report_dashes():
        print(f"-" * 50)

    report_dashes()
    print(f"Interest Earned: ${interest_earned: ,.02f}")
    print(f"Updated Savings Balance: ${updated_savings_balance: ,.02f}")
    report_dashes()

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    # Removed leading and trailing spaces
    # Type casting the user input
    # Valiadting that the value is non-negitive.  
    # In the future, ui can be enhanced  
    cd_balance_in = float(input("Initial CD Balance: ").strip())
    cd_balance = validate_positive_num_account_input(cd_balance_in)

    cd_interest_in = float(input("Interest Rate: ").strip())
    cd_interest = validate_positive_num_account_input(cd_interest_in)

    cd_maturity_in = int(input("Number of months for the CD Account: ").strip())
    cd_maturity = validate_positive_num_account_input(cd_maturity_in)


    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    # In the future, ui can be enhanced.
    report_dashes()
    print(f"Interest Earned: ${interest_earned: ,.02f}")
    print(f"Updated CD Balance: ${updated_cd_balance: ,.02f}")
    report_dashes()

if __name__ == "__main__":
    # Call the main function.
    main()
