from typing import List


def enterprise_value_from_multiple(metric: float, multiple: float) -> float:
    """Estimate Enterprise Value using a valuation multiple (e.g. EV/EBITDA)."""
    return metric * multiple


def implied_equity_value(enterprise_value: float, net_debt: float) -> float:
    """Convert Enterprise Value to Equity Value."""
    return enterprise_value - net_debt


def peer_valuation_range(metric: float, peer_multiples: List[float]) -> List[float]:
    """Generate a valuation range based on a list of peer multiples."""
    return [metric * m for m in peer_multiples]
