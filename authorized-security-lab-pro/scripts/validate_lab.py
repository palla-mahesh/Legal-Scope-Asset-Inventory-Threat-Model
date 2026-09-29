#!/usr/bin/env python3
import csv, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

required = [
    "README.md",
    "requirements.txt",
    "config/asset_inventory.csv",
    "config/engagement.json",
    "docs/AUTHORIZED_LAB_DOSSIER.md",
    "docs/RULES_OF_ENGAGEMENT.md",
    "docs/STRIDE_REGISTER.md",
    "docs/data_flow.dot",
    "docs/data_flow.md",
    "docs/FINDING_TEMPLATE.md",
    "docs/DELIVERABLES.md",
    "app/vulnerable_lab.py",
    "app/dashboard.py",
    "scripts/scope_recon.py"
]

errors = []

for rel in required:
    if not (ROOT / rel).exists():
        errors.append("Missing: " + rel)

with open(ROOT / "config/asset_inventory.csv", newline="") as f:
    rows = list(csv.DictReader(f))

expected = {"LAB-01", "LAB-02"}
actual = {row["asset_id"] for row in rows}

if actual != expected:
    errors.append(f"Inventory IDs must be {sorted(expected)}; found {sorted(actual)}")

for row in rows:
    if row["testing_allowed"].strip().lower() != "yes":
        errors.append(f"{row['asset_id']} is not marked testing_allowed=Yes")

with open(ROOT / "config/engagement.json") as f:
    engagement = json.load(f)

for asset in expected:
    if asset not in engagement["approved_assets"]:
        errors.append(f"{asset} missing from approved_assets")

if errors:
    print("VALIDATION FAILED")
    for error in errors:
        print(" -", error)
    sys.exit(1)

print("VALIDATION PASSED")
print("Approved assets:", ", ".join(sorted(actual)))
print("Scope enforcement is configured for LAB-01 and LAB-02.")
