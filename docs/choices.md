
# Best-Choices Profiles (2025) — and how to change them

We ship with pragmatic defaults in `config/choices_default.yaml`:

- **L1 (mini-magnetosphere):** REBCO HTS coil ~10 T, 1 m standoff; water/CO₂ plasma feed ~1 g/min.
- **L2 (laser mitigation):** liquid-sheet plasma mirror (R_PM≈0.6), tapered-fiber SBS PCM (R_SBS≈0.75), chi≈0.2.
- **L3 (kinetics):** stuffed Whipple with **UHMWPE** fabric (~5 mm) between Al bumper and rear wall; standoff 0.5 m.
- **RF:** SE=40 dB, filters=20 dB, cables=10 dB; target margin 20 dB; allowed 140 dBµV/m.

## Override strategy

1. **Temporary scenario-specific change:** edit the YAML in `scenarios/*.yaml` (only the keys you need).
2. **Global repo default change:** edit `config/choices_default.yaml`.
3. **External profile:** create your own YAML (say `my_choices.yaml`) and use:
   - Calculator: `python code/cest_calculator.py --choices my_choices.yaml ...`
   - Sweeps/CI: set env var `AEGIS_CHOICES=/path/to/my_choices.yaml`.

The loader performs a **deep-merge**, so your file only needs keys that differ.
