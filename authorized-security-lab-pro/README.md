# Authorized Security Lab — Pro Version

Kali Linux-ready project for Legal Scope, Asset Inventory & Threat Model.

## Quick start

```bash
sudo apt update
sudo apt install -y python3 python3-venv nmap graphviz

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python3 scripts/validate_lab.py
python3 app/vulnerable_lab.py
```

Open the local training application at:
http://127.0.0.1:8080

Run the documentation dashboard in another terminal:
```bash
source .venv/bin/activate
python3 app/dashboard.py
```

Dashboard:
http://127.0.0.1:9090

Generate the DFD:
```bash
dot -Tpng docs/data_flow.dot -o docs/data_flow.png
```

Only test assets explicitly listed in `config/asset_inventory.csv`.
