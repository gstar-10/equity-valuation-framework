from typing import Dict, List, Tuple
from .dcf_model import project_fcfs, dcf_valuation


def stress_test_dcf(
    base_inputs: Dict[str, float],
    revenue_growth_grid: List[float],
    discount_rate_grid: List[float],
    terminal_growth: float,
) -> List[Tuple[float, float, float]]:
    """
    Run a 2D stress test over revenue growth and discount rate.
    Returns list of tuples: (revenue_growth, discount_rate, enterprise_value).
    """
    results = []

    for g in revenue_growth_grid:
        for r in discount_rate_grid:
            fcfs = project_fcfs(
                initial_revenue=base_inputs["initial_revenue"],
                revenue_growth=g,
                ebit_margin=base_inputs["ebit_margin"],
                tax_rate=base_inputs["tax_rate"],
                reinvestment_rate=base_inputs["reinvestment_rate"],
                years=int(base_inputs["years"]),
            )

            ev = dcf_valuation(
                fcfs=fcfs,
                discount_rate=r,
                terminal_growth=terminal_growth,
            )

            results.append((g, r, ev))

    return results
