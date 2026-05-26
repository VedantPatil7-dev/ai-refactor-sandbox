def check_investment_return(principal_amount, annual_interest_rate, number_of_years):
    """
    Calculates the future value of an investment using compound interest and
    determines if it yields a high or low return based on a threshold.

    Args:
        principal_amount (float): The initial amount of money invested.
        annual_interest_rate (float): The annual interest rate as a decimal (e.g., 0.05 for 5%).
        number_of_years (int): The number of years the money is invested.

    Returns:
        float: The calculated future value of the investment.
    """
    # Define the threshold for what constitutes a "high return".
    # This constant could be passed as an argument or defined globally if used elsewhere.
    HIGH_RETURN_THRESHOLD = 10000.0

    # Calculate the future value of the investment using the compound interest formula:
    # FV = P * (1 + r)^n
    # Where:
    #   FV = Future Value
    #   P  = Principal Amount
    #   r  = Annual Interest Rate
    #   n  = Number of Years
    future_value = principal_amount * (1 + annual_interest_rate) ** number_of_years

    # Determine if the investment's future value exceeds the high-return threshold.
    if future_value > HIGH_RETURN_THRESHOLD:
        print("high return")
    else:
        print("low return")

    # Return the calculated future value for further use.
    return future_value