# Define a constant for the minimum future value considered a "high return".
HIGH_RETURN_THRESHOLD = 10000

def check_investment_return(principal_amount, annual_interest_rate, number_of_years):
    # Calculate the future value of the investment using the compound interest formula.
    # Formula: FV = P * (1 + r)^n, where:
    # FV = Future Value
    # P = Principal Amount (initial investment)
    # r = Annual Interest Rate (as a decimal)
    # n = Number of Years the investment is held
    future_value = principal_amount * (1 + annual_interest_rate) ** number_of_years

    # Determine if the calculated future value meets or exceeds the high return threshold.
    if future_value > HIGH_RETURN_THRESHOLD:
        print("high return") # Output message indicating a high return.
    else:
        print("low return") # Output message indicating a low return.

    # Return the calculated future value of the investment.
    return future_value