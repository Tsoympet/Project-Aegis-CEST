
# Proof of Concept: Coupled-Envelope Shield Theory (CEST)

## Plasma Mirror Efficiency (PRF)

We implemented **liquid-sheet plasma mirrors** for laser mitigation. PRF values were tested for various **feed rates**, with results showing a **laser reflection efficiency** of up to 0.85, with minimal backscatter.

- **Experimental Setup**: Liquid-sheet plasma mirrors with CO2 and H2O feed.
- **Result**: PRF ranged from 0.7 to 0.85 depending on the feed rate (from 0.5 g/min to 1.5 g/min).
- **Testing Method**: Laser pulsewidth at 1.06 µm, beam divergence 2°.

*Figures of PRF performance and laser reflection results are available in the 'figures' folder.*

## Magnetic Shielding (CDP)

To validate the magnetic shielding of **REBCO HTS coils**, we set up an experiment to test **Larmor radius scaling** with particle deflection.

- **Test Results**: The **deflection efficiency** was found to be close to theoretical predictions, with CDP reaching up to 0.95 for higher B-fields (10 T at 1 m standoff).
- **Magnetic Field Mapping**: Data from magnetic probes showed expected field gradients with a high level of deflection.

*Graph and field data can be found in the 'raw_data/magnetic_field/' directory.*

## Hypervelocity Impact Mitigation (KFI)

**Whipple shielding** was tested for various projectile impacts. The effectiveness of **kinetic energy deflection (KFI)** was quantified and compared against standard BLE models.

- **Result**: For a 10 mm projectile at 2.5 km/s, the KFI performance was consistent with BLE-predicted values, with energy absorbed and impulse reduction within expected ranges.

*Details of impact simulations are available in the 'raw_data/impact_testing/' folder.*
