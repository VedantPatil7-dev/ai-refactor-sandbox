def check_investment_return(principal_amount, annual_interest_rate, number_of_years):
    # Define the monetary threshold that determines a high return.
    HIGH_RETURN_THRESHOLD = 10000.0

    # Calculate the future value of the investment using the compound interest formula.
    # Formula: P * (1 + r)^n, where P is principal, r is annual rate, n is number of years.
    future_value = principal_amount * (1 + annual_interest_rate) ** number_of_years

    # Determine if the investment's future value surpasses the high-return threshold.
    if future_value > HIGH_RETURN_THRESHOLD:
        print("Investment shows a high potential return.")
    else:
        print("Investment shows a low potential return.")

    # Return the calculated future value of the investment.
    return future_value