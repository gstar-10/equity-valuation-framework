import numpy as np


def discount_factor(rate: float, period: int) -> float:
    """
    Calculate the discount factor for a given rate and time period.
    """
    return 1 / ((1 + rate) ** period)


def present_value(cash_flow: float, rate: float, period: int) -> float:
    """
    Discount a single future cash flow back to present value.
    """
    return cash_flow * discount_factor(rate, period)


def wacc_from_market_values(equity_value: float,
                            debt_value: float,
                            cost_of_equity: float,
                            cost_of_debt: float,
                            tax_rate: float) -> float:
    """
    Calculate Weighted Average Cost of Capital (WACC)
    using market value weights.
    """
    total_value = equity_value + debt_value
    return (
        (equity_value / total_value) * cost_of_equity
        + (debt_value / total_value) * cost_of_debt * (1 - tax_rate)
    )


def terminal_value_gordon(final_fcf: float,
                          wacc: float,
                          growth_rate: float) -> float:
    """
    Calculate terminal value using the perpetual growth (Gordon) model.
    """
    if growth_rate >= wacc:
        raise ValueError("Growth rate must be less than WACC.")
    return final_fcf * (1 + growth_rate) / (wacc - growth_rate)


def terminal_value_exit_multiple(metric: float,
                                 multiple: float) -> float:
    """
    Calculate terminal value using an exit multiple method.
    """
    return metric * multiple
