def calculate_investment_performance(initial_investment, yearly_interest_rate, investment_duration_years):
    """
    Calculates the future value of an investment based on compound interest
    and categorizes its return as high or low compared to a threshold.

    Args:
        initial_investment (float): The principal amount invested.
        yearly_interest_rate (float): The annual interest rate (as a decimal).
        investment_duration_years (int): The number of years the investment will grow.

    Returns:
        float: The calculated future value of the investment.
    """
    # Define the threshold for considering an investment as "high return".
    HIGH_RETURN_THRESHOLD = 10000.0

    # Calculate the future value using the compound interest formula:
    # Future Value = Principal * (1 + Interest Rate) ^ Number of Years
    future_investment_value = initial_investment * (1 + yearly_interest_rate) ** investment_duration_years

    # Compare the calculated future value against the defined threshold.
    if future_investment_value > HIGH_RETURN_THRESHOLD:
        print("Investment shows a high return.")
    else:
        print("Investment shows a low return.")

    # Return the calculated future value for potential further analysis.
    return future_investment_value