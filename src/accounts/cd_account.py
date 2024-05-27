# src/accounts/cd_accounts.py

# This contains the cd account business logic

"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
# Dependencies: Import the Account class from the Account module
from .Account import Account as acct


def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    # Create a CD Account object and initialize balance and interest rate with floats
    cd_account = acct(balance=0.0,interest=0.0)
    cd_account.set_balance(balance)
    cd_account.set_interest(interest_rate)

    # Calculate interest earned
    # ADD YOUR CODE HERE
    # interest = balance * (apr/100 * months/12) // Formula hint in step 2 of the 'Create the Savings Account Function' section
      # the APR is directly given as the interest rate and so explicitly assigning here for clarity
    apr = interest_rate
    interest_earned = balance * (apr/100 * months/12)

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_balance = cd_account.balance + interest_earned
    
    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    cd_account.set_balance(updated_balance)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    cd_account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return cd_account.balance, cd_account.interest # ADD YOUR CODE HERE

def main():
    """Functional test of: create_cd_account(balance, interest_rate, months)  
    
    Args:
        balance = 2000  # initial balance
        interest_rate = 4  # 4% apr
        months = 12  # duration in months

    Expected results:
        Updated Balance: $ 2,080.00
        Interest Earned: $ $80.00
    """
    balance = 2000  # initial balance
    interest_rate = 4  # 4% apr
    months = 12  # duration in months

    updated_balance, interest_earned = create_cd_account(balance, interest_rate, months)
    print(f"Updated Balance: ${updated_balance: ,.2f}")  # expecting $ 2,080.00
    print(f"Interest Earned: ${interest_earned: ,.2f}")  # expecting $ $80.00


if __name__ == "__main__":
    main()