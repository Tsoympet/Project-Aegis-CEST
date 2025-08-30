
# Project Aegis: Coupled-Envelope Shield Theory (CEST)

This repository implements the **Coupled-Envelope Shield Theory (CEST)**, a unified theory that couples **plasma mirrors**, **SBS phase-conjugation**, and **Whipple impact mitigation** for spacecraft shields. CEST helps to evaluate multi-layer defenses against **lasers**, **charged particle flux**, and **hypervelocity debris**.

## Theory Overview

CEST introduces a measurable bound on absorbed energy and impulse at the hull:
```
\dot E_{\mathrm{abs}} \le (1-\mathrm{PRF}) \cdot \dot E_{\mathrm{laser}} + (1-\mathrm{CDP}) \cdot \dot E_{\mathrm{charged}} + (1-\mathrm{KFI}) \cdot \dot E_{\mathrm{kinetic}}
```

Where:
- **PRF**: Plasma rejection for laser mitigation
- **CDP**: Charged particle deflection for magnetic shield
- **KFI**: Kinetic impact mitigation via multi-layered Whipple shield

## Installation

Clone the repository:
```bash
git clone https://github.com/YOUR_USER/YOUR_REPO.git
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Use the calculator and run sweeps:
```bash
python code/cest_calculator.py --laser_kw 120 --kinetic_kw 15
python code/run_sweep.py scenarios/demo.yaml
```

For more details on how to adjust parameters, please refer to **choices.md** and **ethics.md**.
