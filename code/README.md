# Project Aegis CEST Code

## Overview
This repository contains the scripts necessary to simulate and analyze spacecraft shielding using the **Coupled-Envelope Shield Theory (CEST)**. The framework integrates plasma mirrors, magnetic shielding, and Whipple shields into a unified performance analysis.

## Requirements
- Python 3.x
- Required libraries: `numpy`, `matplotlib`, `yaml`

## Files
- **`cest_calculator.py`**: Main script for calculating shield effectiveness.
- **`run_sweep.py`**: Script to run multiple scenarios and sweep parameters.
- **`config/choices_default.yaml`**: Default configuration file.

## How to Run the Calculator
You can run the calculator using the following command:
```bash
python code/cest_calculator.py --laser_kw 100 --charged_kw 30
