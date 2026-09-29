# Legal-Scope-Asset-Inventory-Threat-Model

### `README.md`

````markdown
# Authorized Security Lab — Pro Version

A Kali Linux-ready security engagement project for:

**Legal Scope, Asset Inventory & Threat Model**

This project provides a controlled, isolated security-testing laboratory with
documentation, asset inventory, threat modeling, rules of engagement, evidence
handling, and scope-controlled reconnaissance.

---

## Project Objectives

The project is designed to provide the following deliverables:

- Written authorization / lab dossier
- Authorized asset inventory
- Local intentionally vulnerable training application
- Data-flow diagram
- STRIDE threat model
- Rules of engagement
- Testing-window and stop-condition framework
- Evidence-handling structure
- Security finding/report template
- Scope-controlled Nmap reconnaissance
- Automated project validation
- Security documentation dashboard

---

# Project Structure

```text
authorized-security-lab-pro/
│
├── README.md
├── requirements.txt
│
├── app/
│   ├── vulnerable_lab.py
│   └── dashboard.py
│
├── config/
│   ├── asset_inventory.csv
│   └── engagement.json
│
├── docs/
│   ├── AUTHORIZED_LAB_DOSSIER.md
│   ├── RULES_OF_ENGAGEMENT.md
│   ├── STRIDE_REGISTER.md
│   ├── data_flow.md
│   ├── data_flow.dot
│   ├── FINDING_TEMPLATE.md
│   └── DELIVERABLES.md
│
├── scripts/
│   ├── scope_recon.py
│   └── validate_lab.py
│
└── evidence/
    └── README.md
````

---

# 1. Requirements

The project is designed to run on Kali Linux.

Install the required packages:

```bash
sudo apt update
sudo apt install -y python3 python3-venv nmap graphviz
```

Check the installations:

```bash
python3 --version
nmap --version
dot -V
```

---

# 2. Create Python Virtual Environment

Navigate to the project:

```bash
cd ~/authorized-security-lab-pro
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

---

# 3. Validate the Project

Before starting the lab, run:

```bash
python3 scripts/validate_lab.py
```

Expected output:

```text
VALIDATION PASSED
Approved assets: LAB-01, LAB-02
Scope enforcement is configured for LAB-01 and LAB-02.
```

If validation fails, correct the reported issue before testing.

---

# 4. Authorized Assets

The project contains two authorized laboratory assets.

| Asset ID | Target           | Environment                     |
| -------- | ---------------- | ------------------------------- |
| LAB-01   | `127.0.0.1:8080` | Localhost training application  |
| LAB-02   | `192.168.56.20`  | Private host-only vulnerable VM |

The authoritative inventory is:

```text
config/asset_inventory.csv
```

Only assets explicitly listed in the inventory should be tested.

---

# 5. Start the Vulnerable Training Application

Start LAB-01:

```bash
python3 app/vulnerable_lab.py
```

The application runs on:

```text
http://127.0.0.1:8080
```

You should see:

```text
* Serving Flask app 'vulnerable_lab'
* Debug mode: off
* Running on http://127.0.0.1:8080
```

---

# 6. Test the Application

Open a browser and visit:

```text
http://127.0.0.1:8080
```

Available training endpoints:

```text
/
 /health
 /search
 /login
 /profile
```

Check the health endpoint:

```bash
curl http://127.0.0.1:8080/health
```

Expected response:

```json
{
  "lab": "authorized",
  "scope": "LAB-01",
  "status": "ok"
}
```

---

# 7. If Port 8080 Is Already in Use

Check the process:

```bash
sudo ss -ltnp | grep :8080
```

You can also use:

```bash
sudo lsof -i :8080
```

If the existing process is the training application, do not start another
instance.

Test it directly:

```bash
curl http://127.0.0.1:8080/health
```

If the health response is returned, LAB-01 is already running.

---

# 8. Start the Documentation Dashboard

Open another terminal.

Activate the virtual environment:

```bash
cd ~/authorized-security-lab-pro
source .venv/bin/activate
```

Start the dashboard:

```bash
python3 app/dashboard.py
```

The dashboard runs at:

```text
http://127.0.0.1:9090
```

Open it using:

```bash
xdg-open http://127.0.0.1:9090
```

The dashboard displays:

* Authorized assets
* Testing status
* Stop conditions
* Project deliverables

---

# 9. Data-Flow Diagram

The Graphviz source is:

```text
docs/data_flow.dot
```

Generate the PNG:

```bash
dot -Tpng docs/data_flow.dot -o docs/data_flow.png
```

Verify the image:

```bash
ls -lh docs/data_flow.png
```

Open it:

```bash
xdg-open docs/data_flow.png
```

The generated file is:

```text
docs/data_flow.png
```

---

# 10. Scope-Controlled Reconnaissance

The project includes a scope-controlled Nmap script.

The script reads:

```text
config/asset_inventory.csv
```

and verifies that the requested asset is authorized.

## LAB-01

Run:

```bash
sudo python3 scripts/scope_recon.py --asset LAB-01 --ports 80,443,8080
```

## LAB-02

Run:

```bash
sudo python3 scripts/scope_recon.py --asset LAB-02 --ports 22,80,443,8080
```

The script uses low-rate reconnaissance.

Do not modify it to scan arbitrary third-party systems.

---

# 11. Authorized Lab Dossier

The authorization documentation is located at:

```text
docs/AUTHORIZED_LAB_DOSSIER.md
```

It contains:

* Lab owner
* Assessor
* Approval date
* Authorized assets
* Permitted activities
* Explicit exclusions
* Testing window
* Stop conditions
* Evidence handling
* Reporting requirements

Before actual testing, complete:

```text
approval_date
testing_window.start
testing_window.end
```

in:

```text
config/engagement.json
```

---

# 12. Rules of Engagement

The Rules of Engagement document is:

```text
docs/RULES_OF_ENGAGEMENT.md
```

The engagement permits controlled activities such as:

* Asset discovery
* Service identification
* Low-rate reconnaissance
* HTTP validation
* Non-destructive training validation
* Evidence collection
* Threat modeling
* Security reporting

---

# 13. Prohibited Activities

The following activities are outside this laboratory project:

```text
Denial of Service
Destructive payloads
Persistence
Credential reuse
Third-party target testing
Uncontrolled data extraction
Production system testing
Internet-wide scanning
```

Testing must remain inside the authorized laboratory scope.

---

# 14. STRIDE Threat Model

The threat model is located at:

```text
docs/STRIDE_REGISTER.md
```

It covers:

```text
S - Spoofing
T - Tampering
R - Repudiation
I - Information Disclosure
D - Denial of Service
E - Elevation of Privilege
```

Each threat includes:

* Threat category
* Component
* Abuse case
* Potential impact
* Mitigation
* Verification method

---

# 15. Evidence Handling

Evidence should be stored in:

```text
evidence/
```

The evidence directory contains:

```text
evidence/README.md
```

Only the minimum evidence required to support a finding should be collected.

Do not store:

* Real credentials
* Unnecessary personal information
* Unrelated files
* Production data

Redact sensitive information before including evidence in the final report.

---

# 16. Security Finding Template

Use:

```text
docs/FINDING_TEMPLATE.md
```

Each security finding should contain:

```text
Asset
Severity rationale
Reproduction steps
Impact
Evidence
Remediation
Retest status
```

---

# 17. Final Deliverables

The complete deliverable list is available in:

```text
docs/DELIVERABLES.md
```

The final project should contain:

```text
✓ Authorized Lab Dossier
✓ Asset Inventory
✓ Intentionally Vulnerable Lab
✓ Data-Flow Diagram
✓ STRIDE Threat Register
✓ Rules of Engagement
✓ Scope-Controlled Reconnaissance
✓ Evidence Handling
✓ Finding Template
✓ Validation Script
✓ Documentation Dashboard
```

---

# 18. Recommended Execution Order

Follow this sequence:

```text
Step 1
  ↓
Install Kali dependencies
  ↓
Step 2
  ↓
Create Python virtual environment
  ↓
Step 3
  ↓
Install requirements
  ↓
Step 4
  ↓
Run validation
  ↓
Step 5
  ↓
Start LAB-01
  ↓
Step 6
  ↓
Verify /health
  ↓
Step 7
  ↓
Generate Data-Flow Diagram
  ↓
Step 8
  ↓
Run authorized reconnaissance
  ↓
Step 9
  ↓
Review STRIDE threats
  ↓
Step 10
  ↓
Document findings
  ↓
Step 11
  ↓
Collect minimal evidence
  ↓
Step 12
  ↓
Complete final report
```

---

# 19. Quick Start

For a fresh Kali installation:

```bash
cd ~/authorized-security-lab-pro

sudo apt update
sudo apt install -y python3 python3-venv nmap graphviz

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python3 scripts/validate_lab.py
```

Start the lab:

```bash
python3 app/vulnerable_lab.py
```

In another terminal:

```bash
cd ~/authorized-security-lab-pro
source .venv/bin/activate

curl http://127.0.0.1:8080/health
```

Generate the DFD:

```bash
dot -Tpng docs/data_flow.dot -o docs/data_flow.png
```

Open the DFD:

```bash
xdg-open docs/data_flow.png
```

Start the dashboard:

```bash
python3 app/dashboard.py
```

Open:

```text
http://127.0.0.1:9090
```

---

# 20. Project Completion Checklist

Before submitting the project, verify:

```text
[ ] Written authorization completed
[ ] Approval date completed
[ ] Testing window completed
[ ] Lab owner confirmed
[ ] Assessor confirmed
[ ] Asset inventory reviewed
[ ] LAB-01 tested only locally
[ ] LAB-02 confirmed as host-only lab
[ ] Data-flow diagram generated
[ ] STRIDE register completed
[ ] Rules of Engagement reviewed
[ ] Evidence redacted
[ ] Findings documented
[ ] Remediation documented
[ ] Validation script passes
[ ] Final deliverables reviewed
```
