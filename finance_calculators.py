# Import required modules:
import math

# Hard-code strings for calculation types
# These are separate for ease of editing
bond = "bond"
investment = "investment"

# Apply .casefold() method and write back to same variables for consistent
# comparison
bond = bond.casefold()
investment = investment.casefold()

# Hard-code messages from specification
investment_describe = \
"to calculate the amount of interest you'll earn on your investment"
bond_describe = "to calculate the amount you'll have to pay on a home loan"

# Hard-code choice line, separate for ease of editing.
# If editing, please note that a new line character is added later.
choose = "Enter either 'investment' or 'bond' from the menu above to proceed:"

#   Get length of longest calculation type string to produce separate, 
# strings describing calculations with consistent column spacing.
col_length = max(len(investment), len(bond))

# print lines 1 and 2 using above messages:
print (investment.ljust(col_length), investment_describe, sep = " - ")
print (bond.ljust(col_length), bond_describe, sep = " - ")

# print blank line as specified
print()

# Ask user which calculation is required, save as case-folded string
# The use of `.casefold()` ensures case-insensitive matching.
calculation_type = input(choose+"\n").casefold()

if calculation_type == investment:
#TODO
    print("Investment partial TODO")
    # Ask user for the amount that they wish to invest, cast to float and 
    # store as `amount`
    amount = float(input(
        "How much money do you wish to deposit? "
        ))
    
    #   Ask user for the annual interest rate, cast to float, divide by 100 
    # to obtain rate as fraction and store as `amount`
    annual_rate = float(input(
        "What is the expected annual rate in percent? "
    )) / 100
    
    # Ask user for number of years that the user intends the investment 
    # to be for. Cast to integer and store as n_years (n following 
    # mathematical convention of n for integers)
    n_years = int(input(
        "How many years do you plan to invest for? "
        ))
    
    # Ask if interest is to be simple or compound:
    # Cast to casefold for ease of comparison
    interest_type = input("Is the interest simple or compound?").casefold()
    
    #   Perform calculation using specified formulae as required, save result
    # as variable `result` so that a single print statement may be used.
    if interest_type == "simple".casefold():
        result = amount * (1 + annual_rate * n_years)
    else:
        result = amount * math.pow(1 + annual_rate, n_years)
        
    # Finally, print result (to 2dp) to screen.
    print (
        f"The value of your investment is expected to be about {result:.2f}"
        )

elif calculation_type == bond:
    #   First obtain the value of loan to repay from the user. Cast to float and 
    #store as `to_repay`.
    to_repay = float(input("How much is the loan to be repaid? "))
    
    #   Then obtain the annual interest rate in percent. Cast to float, divide 
    #by 1200 in order to give the fraction-equivalent monthly rate and store 
    #as `monthly_rate`.
    monthly_rate = float(input(
        "What is the simple annual loan rate in percent? "
    )) / 1200
    
    # Obtain the planned number of repayment months, cast to integer 
    # and store as `months_payment`.
    repay_months = int(input(
        "Over how many months do you intend to repay the loan? "
        ))
    
    #   Calculate the monthly repayment, store as variable `result` for 
    #later output to screen.
    result = (monthly_rate * to_repay) / \
        (1 - (1+monthly_rate)**(-repay_months))
    
    # Print result to screen, rounded to two decimal places.
    print(f"The expected monthly repayment is about {result:.2f}")
    
else:
# Runs help message if an improper or no choice specified by user.
    print("Sorry, you did not choose a valid calculation type")
    print("Please re-run this script")