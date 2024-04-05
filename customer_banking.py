# Import the create_cd_account and create_savings_account functions
from cd_account.py import create_cd_account
from savings_account.py import create_savings_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = input("What is the balance of your account?")
    interest = input("What is the interest rate?")
    months = input("For how long (in months)")

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, interest, months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print('{:,.0f}'.format(interest))
    print('{:,.0f}'.format(balance))
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = input("What is the balance of your CD?")
    interest = input("What is the interest rate?")
    months = input("For how long (in months)")
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, interest, months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # Printing was added to the module already
    print('{:,.0f}'.format(interest))
    print('{:,.0f}'.format(balance))
    
if __name__ == "__main__":
    # Call the main function.
    main()

