from typing import List
from .utils import present_value, terminal_value_gordon


def project_fcfs(
    initial_revenue: float,
    revenue_growth: float,
    ebit_margin: float,
    tax_rate: float,
    reinvestment_rate: float,
    years: int,
) -> List[float]:
    """
    Project Free Cash Flows over a forecast period.
    """
    fcfs = []
    revenue = initial_revenue

    for _ in range(years):
        revenue *= (1 + revenue_growth)
        ebit = revenue * ebit_margin
        nopat = ebit * (1 - tax_rate)
        reinvestment = nopat * reinvestment_rate
        fcf = nopat - reinvestment
        fcfs.append(fcf)

    return fcfs


def dcf_valuation(
    fcfs: List[float],
    discount_rate: float,
    terminal_growth: float,
) -> float:
    """
    Perform DCF valuation including terminal value.
    """
    enterprise_value = 0

    for t, fcf in enumerate(fcfs, start=1):
        enterprise_value += present_value(fcf, discount_rate, t)

    terminal_fcf = fcfs[-1]
    terminal_value = terminal_value_gordon(
        terminal_fcf,
        discount_rate,
        terminal_growth,
    )

    enterprise_value += present_value(
        terminal_value,
        discount_rate,
        len(fcfs),
    )

    return enterprise_value
