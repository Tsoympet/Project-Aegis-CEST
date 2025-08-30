# Project Aegis CEST

This repository implements the **Coupled-Envelope Shield Theory (CEST)** for spacecraft protection against **laser**, **charged-particle**, and **hypervelocity debris** threats.

## Key Features
- **Theory and Methodology** for multi-layer shield effectiveness.
- **Scenario-based sweeps** for shield performance under mixed threats.
- **Python-based calculator** for scenario analysis.
- **Open-source repository** with reproducible results.

## Getting Started

Clone the repository and follow the instructions below to run the calculator and simulate scenarios.

### Prerequisites
Make sure you have **Python 3.x** installed, along with **pip** (Python's package manager).

Install dependencies:
```bash
pip install -r requirements.txt

Running the Calculator

To run the calculator with different parameters, use the following command:
python code/cest_calculator.py --laser_kw 100 --charged_kw 30

For running multiple scenarios, you can use the run_sweep.py script with a YAML file defining configurations.
python -m unittest discover -s tests

To run unit tests, use the following command:
python -m unittest discover -s tests
