def check_investment_return(principal_amount, annual_interest_rate, number_of_years):
    # Calculate the future value of the investment using the compound interest formula.
    # Formula: P * (1 + r)^n, where P is principal, r is rate, n is years.
    future_value = principal_amount * (1 + annual_interest_rate) ** number_of_years

    # Determine if the investment's future value exceeds a predefined high-return threshold.
    if future_value > 10000:
        print("high return")
    else:
        print("low return")

    # Return the calculated future value of the investment.
    return future_value