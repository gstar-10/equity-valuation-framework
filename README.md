# Equity Valuation Framework

A modular equity valuation framework built in Python.

This project implements:

- Discounted Cash Flow (DCF) modelling
- Comparable company valuation (multiples-based)
- Enterprise to equity bridge
- Sensitivity and stress testing
- Modular financial utilities (WACC, discounting, terminal value)



## Features

### 1. DCF Model
Projects free cash flows based on:
- Revenue growth
- Operating margin
- Tax rate
- Reinvestment rate

Enterprise value is calculated using:
- Explicit forecast period
- Terminal value (Gordon Growth)
- Discounted using WACC



### 2. Comparable Company Analysis
- EV/EBITDA style multiple valuation
- Peer valuation range generation
- Enterprise → Equity bridge



### 3. Stress Testing
Performs 2D grid sensitivity analysis over:
- Revenue growth assumptions
- Discount rate assumptions

Returns valuation surface for scenario analysis.



## Why This Project?

This framework was built to replicate real-world equity research and investment banking valuation workflows in a clean, modular Python structure.

Designed to demonstrate:
- Financial modelling logic
- Code modularity
- Quantitative reasoning
- Scenario analysis capability


---

## Example Usage

```python
from src.dcf_model import project_fcfs, dcf_valuation

fcfs = project_fcfs(
    initial_revenue=100,
    revenue_growth=0.05,
    ebit_margin=0.25,
    tax_rate=0.20,
    reinvestment_rate=0.40,
    years=5
)

enterprise_value = dcf_valuation(
    fcfs=fcfs,
    discount_rate=0.10,
    terminal_growth=0.02
)

print("Enterprise Value:", enterprise_value)

## Future Extensions

- Monte Carlo simulation
- LBO model integration
- Data pipeline integration (API-based financial data)
- Visualization dashboard
