from typing import List


def enterprise_value_from_multiple(
    metric: float,
    multiple: float
) -> float:
    """
    Estimate enterprise value using a valuation multiple
    (e.g. EV/EBITDA).
    """
    return metric * multiple


def implied_equity_value(
    enterprise_value: float,
    net_debt: float
) -> float:
    """
    Convert enterprise value to equity value.
    """
    return enterprise_value - net_debt


def peer_valuation_range(
    metric: float,
    peer_multiples: List[float]
) -> List[float]:
    """
    Generate valuation range based on peer multiples.
    """
    return [metric * multiple for multiple in peer_multiples]
