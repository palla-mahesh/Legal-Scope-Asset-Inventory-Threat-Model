#!/usr/bin/env python3
import argparse, csv, ipaddress, shutil, subprocess, sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "config/asset_inventory.csv"

def load_inventory():
    with open(INV, newline="") as f:
        return {r["asset_id"]: r for r in csv.DictReader(f)}

def target_from_row(row):
    value = row["ip_or_url"].strip()
    if value.startswith(("http://", "https://")):
        return urlparse(value).hostname
    return value

def main():
    parser = argparse.ArgumentParser(
        description="Run low-rate Nmap reconnaissance on an approved asset."
    )
    parser.add_argument("--asset", required=True, choices=["LAB-01", "LAB-02"])
    parser.add_argument("--ports", default="22,80,443,8080")
    args = parser.parse_args()

    if shutil.which("nmap") is None:
        sys.exit("Nmap is not installed. Install with: sudo apt install -y nmap")

    row = load_inventory()[args.asset]

    if row["testing_allowed"].strip().lower() != "yes":
        sys.exit("Asset is not marked as testing allowed.")

    target = target_from_row(row)

    try:
        ipaddress.ip_address(target)
    except ValueError:
        if target != "localhost":
            sys.exit(f"Refusing non-IP target: {target}")

    if args.asset == "LAB-01" and target not in {"127.0.0.1", "localhost"}:
        sys.exit("LAB-01 scope mismatch.")

    if args.asset == "LAB-02" and target != "192.168.56.20":
        sys.exit("LAB-02 scope mismatch.")

    command = [
        "nmap", "-sT", "-sV", "--version-light",
        "-T2", "-p", args.ports, "--reason", target
    ]

    print("AUTHORIZED ASSET:", args.asset)
    print("TARGET:", target)
    print("COMMAND:", " ".join(command))
    print("Use only during the approved testing window.")
    subprocess.run(command, check=False)

if __name__ == "__main__":
    main()
