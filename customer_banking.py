# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account


# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # Savings account details
    savings_balance = float(input("Enter savings balance: "))
    savings_interest_rate = float(input("Enter savings interest rate: "))
    savings_maturity = int(input("Enter savings months: "))

    # Call the create_savings_account function and pass the variables from the user.
    savings_updated_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest_rate, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Savings Account - Interest Earned: {savings_interest_earned}, Updated Balance: {savings_updated_balance}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("Enter CD balance: "))
    cd_interest_rate = float(input("Enter CD interest rate (%): "))
    cd_maturity = int(input("Enter CD account duration in months: "))


    # Call the create_cd_account function and pass the variables from the user.
    cd_updated_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"CD Account - Interest Earned: {cd_interest_earned}, Updated Balance: {cd_updated_balance}")

 # This is to run main
if __name__ == "__main__":
    
    main()

   
