# Rules of Engagement

## 1. Authorization
Testing is authorized only for assets in config/asset_inventory.csv.

## 2. Scope

### In scope
- 127.0.0.1:8080 — LAB-01
- 192.168.56.20 — LAB-02

### Out of scope
- Internet hosts
- Third-party domains
- Production systems
- Personal devices
- Any IP/URL not listed in the inventory

## 3. Allowed techniques
- Asset/service discovery
- Low-rate TCP connect scanning
- HTTP response validation
- Manual non-destructive validation of training weaknesses
- Evidence collection
- Threat modeling and reporting

## 4. Prohibited techniques
- DoS or stress testing
- Destructive payloads
- Persistence
- Credential reuse
- Third-party scanning
- Uncontrolled data extraction

## 5. Time and rate limits
Use the approved start/end time in config/engagement.json. Keep reconnaissance low-rate.

## 6. Evidence handling
Store minimum necessary evidence. Redact secrets and personal data. Do not store credentials.

## 7. Emergency stop
Stop immediately when a stop condition occurs and notify the lab owner/supervisor.

## 8. Reporting
Every finding must include asset, severity rationale, reproduction steps, impact,
evidence reference, and remediation.
