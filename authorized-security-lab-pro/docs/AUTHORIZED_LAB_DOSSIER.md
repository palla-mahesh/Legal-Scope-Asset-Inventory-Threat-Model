# Authorized Lab Dossier

## Engagement
Legal Scope, Asset Inventory & Threat Model

## Written authorization

| Field | Value |
|---|---|
| Lab owner | RabTech lab |
| Assessor | Student assessor |
| Approval date | YYYY-MM-DD — complete before testing |
| Environment | Isolated training lab |
| Approved assets | LAB-01 and LAB-02 |
| Evidence classification | Confidential training evidence |

Only systems explicitly present in the asset inventory may be tested.

## Approved assets

- LAB-01 — Local training web app — http://127.0.0.1:8080
- LAB-02 — Deliberately vulnerable VM — 192.168.56.20

## Permitted activities

- Lab documentation review
- Low-rate service discovery
- Port/service identification with Nmap
- HTTP response/header validation
- Manual non-destructive validation of training weaknesses
- Minimal evidence capture
- Threat modeling and remediation documentation

## Explicit exclusions

- Denial of service
- Destructive payloads
- Persistence
- Credential reuse
- Third-party targets
- Uncontrolled data extraction

## Testing window

Complete the approved start/end times in config/engagement.json before testing.

## Stop conditions

Immediately stop if the target becomes unstable, traffic could leave the lab, an
unapproved target is identified, unexpected personal/production data is encountered,
destructive/persistence techniques would be needed, or the lab owner requests a stop.

## Evidence

Collect minimum necessary evidence. Redact secrets and personal data. Store evidence
under evidence/ and delete it according to the agreed retention period.

## Reporting

Each finding must record asset, severity rationale, reproduction steps, impact, evidence,
and remediation.
