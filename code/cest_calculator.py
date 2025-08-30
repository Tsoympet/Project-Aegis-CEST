
import argparse
import math
import json
from config import load_choices
from ble_models import kfi_from_projectile

def cdp(p_GeVc=1.7, q=1.0, B=10.0, L=1.0):
    if B <= 0 or L <= 0:
        return 0.0
    rL = p_GeVc/(0.3*B*abs(q))
    return 1.0 - math.exp(-L/rL)

def prf(rpm=0.6, rsbs=0.7, chi=0.2):
    return rpm + (1.0 - rpm) * rsbs * (1.0 - chi)

def kfi_surrogate(sigma=8.0, L=0.5, K=12.0):
    return 1.0 - math.exp(-(sigma*L)/K)

def hpm_emp_margin(E_threat_dBuVpm, SE_db, filter_db, cable_db, allowed_dBuVpm):
    E_fail = allowed_dBuVpm + SE_db + filter_db + cable_db
    return E_fail - E_threat_dBuVpm

def main():
    choices = load_choices()
    ap = argparse.ArgumentParser(description="CEST + BLE + HPM/EMP calculator with editable choices")
    # Threat powers
    ap.add_argument("--laser_kw", type=float, default=None)
    ap.add_argument("--charged_kw", type=float, default=None)
    ap.add_argument("--kinetic_kw", type=float, default=None)
    # L1
    ap.add_argument("--B", type=float, default=None, help="Tesla")
    ap.add_argument("--L", type=float, default=None, help="m standoff for L1")
    ap.add_argument("--p_GeVc", type=float, default=1.7, help="Projectile momentum GeV/c (charged flux proxy)")
    # L2
    ap.add_argument("--rpm", type=float, default=None)
    ap.add_argument("--rsbs", type=float, default=None)
    ap.add_argument("--chi", type=float, default=None)
    # L3 (choose surrogate or BLE inputs)
    ap.add_argument("--use_ble", action="store_true", help="Use BLE-based KFI from projectile params")
    ap.add_argument("--proj_D_mm", type=float, default=None, help="Projectile diameter [mm]")
    ap.add_argument("--proj_V_kms", type=float, default=None, help="Impact velocity [km/s]")
    ap.add_argument("--rho_p", type=float, default=None, help="Projectile density [kg/m^3]")
    ap.add_argument("--tb_mm", type=float, default=None, help="Bumper thickness [mm]")
    ap.add_argument("--Sk_m", type=float, default=None, help="Standoff [m] (kinetic)")
    ap.add_argument("--model", choices=["whipple","stuffed","multisheet"], default="stuffed")
    ap.add_argument("--t_stuff_mm", type=float, default=None, help="Stuffing thickness [mm] for stuffed model")
    # Surrogate KFI if not BLE
    ap.add_argument("--sigma", type=float, default=8.0, help="kg/m^2 Whipple surrogate")
    ap.add_argument("--Lk", type=float, default=0.5, help="m standoff for surrogate")
    # Hull limit
    ap.add_argument("--hull_kw", type=float, default=None, help="Hull thermal limit (kW)")
    # HPM/EMP
    ap.add_argument("--threat_dBuVpm", type=float, default=200.0, help="Incident field strength (dBµV/m)")
    ap.add_argument("--allowed_dBuVpm", type=float, default=None, help="Allowable at victim port (dBµV/m)")
    ap.add_argument("--SE_db", type=float, default=None, help="Shielding effectiveness (dB)")
    ap.add_argument("--filter_db", type=float, default=None, help="Feedthrough filter attenuation (dB)")
    ap.add_argument("--cable_db", type=float, default=None, help="Cable/connector shielding (dB)")
    ap.add_argument("--choices", type=str, default=None, help="Path to choices YAML to override defaults")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    # Override choices if requested
    if args.choices:
        choices = load_choices(override_path=args.choices)

    # Fill defaults from choices when args are None
    laser_kw   = args.laser_kw   if args.laser_kw   is not None else 0.0
    charged_kw = args.charged_kw if args.charged_kw is not None else 0.0
    kinetic_kw = args.kinetic_kw if args.kinetic_kw is not None else 0.0

    B = args.B if args.B is not None else choices["L1"]["coil"]["B_T"]
    L = args.L if args.L is not None else choices["L1"]["coil"]["standoff_m"]

    rpm  = args.rpm  if args.rpm  is not None else choices["L2"]["plasma_mirror"]["R_PM_nominal"]
    rsbs = args.rsbs if args.rsbs is not None else choices["L2"]["sbs_pcm"]["R_SBS_nominal"]
    chi  = args.chi  if args.chi  is not None else choices["L2"]["sbs_pcm"]["chi_dump"]

    # L3 defaults
    proj_D_mm = args.proj_D_mm if args.proj_D_mm is not None else choices["L3"]["projectile_defaults"]["D_mm"]
    proj_V_kms = args.proj_V_kms if args.proj_V_kms is not None else choices["L3"]["projectile_defaults"]["V_kms"]
    rho_p = args.rho_p if args.rho_p is not None else choices["L3"]["projectile_defaults"]["rho_p"]
    tb_mm = args.tb_mm if args.tb_mm is not None else choices["L3"]["bumper"]["tb_mm"]
    Sk_m  = args.Sk_m  if args.Sk_m  is not None else choices["L3"]["standoff_m"]
    t_stuff_mm = args.t_stuff_mm if args.t_stuff_mm is not None else choices["L3"]["stuffing"]["t_mm"]

    hull_kw = args.hull_kw if args.hull_kw is not None else choices["Hull"]["thermal_limit_kW"]

    SE_db = args.SE_db if args.SE_db is not None else choices["RF"]["SE_db"]
    filter_db = args.filter_db if args.filter_db is not None else choices["RF"]["filter_db"]
    cable_db  = args.cable_db  if args.cable_db  is not None else choices["RF"]["cable_db"]
    allowed_dBuVpm = args.allowed_dBuVpm if args.allowed_dBuVpm is not None else choices["RF"]["allowed_dBuVpm"]

    CDP = cdp(p_GeVc=args.p_GeVc, B=B, L=L)
    PRF = prf(rpm=rpm, rsbs=rsbs, chi=chi)

    if args.use_ble:
        KFI = kfi_from_projectile(D=proj_D_mm/1000.0, V=proj_V_kms*1000.0, tb=tb_mm/1000.0, S=Sk_m,
                                  model=args.model, rho_p=rho_p, projectile="Al", bumper="Al",
                                  t_stuff=t_stuff_mm/1000.0)
    else:
        KFI = kfi_surrogate()

    absorbed_kw = (1-PRF)*laser_kw + (1-CDP)*charged_kw + (1-KFI)*kinetic_kw
    pass_cei = absorbed_kw <= hull_kw

    RIM = hpm_emp_margin(args.threat_dBuVpm, SE_db, filter_db, cable_db, allowed_dBuVpm)
    rf_ok = RIM > 0.0

    out = {
        "CDP": CDP, "PRF": PRF, "KFI": KFI,
        "absorbed_kW": absorbed_kw, "hull_limit_kW": hull_kw, "CEI_pass": pass_cei,
        "RIM_dB": RIM, "RF_pass": rf_ok,
        "defaults_used": True
    }
    if args.json:
        print(json.dumps(out, indent=2))
    else:
        print(f"CDP={CDP:.3f}  PRF={PRF:.3f}  KFI={KFI:.3f}")
        print(f"Absorbed ~ {absorbed_kw:.1f} kW  (Hull limit {hull_kw:.1f} kW)  => {'PASS' if pass_cei else 'FAIL'}")
        print(f"RIM={RIM:.1f} dB  => {'RF PASS' if rf_ok else 'RF FAIL'}")

if __name__ == "__main__":
    main()
