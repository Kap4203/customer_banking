# src/accounts/savings_account.py

# This contains the savings account business logic

"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
# Dependencies: Import the Account class from the Account module
from .Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    # Create a Savings Account object and initialize balance and interest rate with floats
    savings_account = Account(balance=0.0, interest=0.0)

    # Set the initial balance and interest values of the account
    savings_account.set_balance(balance)
    savings_account.set_interest(interest_rate)


    # Calculate interest earned
    # ADD YOUR CODE HERE
    # interest = balance * (apr/100 * months/12) // Formula hint in step 2 of the 'Create the Savings Account Function' section
    # the APR is directly given as the interest rate and so explicitly assigning here for clarity
    apr = interest_rate
    interest_earned = balance * (apr/100 * months/12)

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_balance = savings_account.balance + interest_earned

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings_account.set_balance(updated_balance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings_account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return savings_account.balance, savings_account.interest # ADD YOUR CODE HERE


def main():
    """Functional test of: create_savings_account(balance, interest_rate, months)  
    
    Args: Setting user inputs to valiate system
        balance = 1000  # initial balance
        interest_rate = 5  # 5% apr
        months = 6  # duration in months

    Expected results:
        Updated Balance: $ 1,025.00
        Interest Earned: $ $25.00
    """
    balance = 1000  # initial balance
    interest_rate = 5  # 5% apr
    months = 6  # duration in months

    updated_balance, interest_earned = create_savings_account(balance, interest_rate, months)
    print(f"Updated Balance: ${updated_balance: ,.2f}")  # expecting $ 1,025.00
    print(f"Interest Earned: ${interest_earned: ,.2f}")  # expecting $ $25.00


if __name__ == "__main__":
    main()