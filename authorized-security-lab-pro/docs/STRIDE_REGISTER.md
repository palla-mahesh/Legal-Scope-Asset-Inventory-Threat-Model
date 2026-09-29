# STRIDE Threat Register

Scope: LAB-01 local training web application and its local request/data flow.

| ID | STRIDE | Component | Abuse Case | Potential Impact | Mitigation | Verification |
|---|---|---|---|---|---|---|
| S-01 | Spoofing | Login | Attempt to act as another user | Unauthorized access | Strong authentication and session controls | Review authentication/session tests |
| T-01 | Tampering | Request parameters | Untrusted input changes application behavior | Integrity loss | Parameterized queries and output encoding | Safe benign validation |
| R-01 | Repudiation | Logs | Actions cannot be attributed reliably | Weak auditability | Structured logs and event IDs | Inspect test events |
| I-01 | Information Disclosure | Errors | Errors expose internal details | Information leakage | Generic errors and detailed server logs | Trigger benign invalid request |
| D-01 | Denial of Service | Web service | Excessive requests exhaust resources | Availability loss | Rate limiting and bounded processing | Configuration review; no stress testing |
| E-01 | Elevation of Privilege | Authorization | Low privilege reaches admin action | Unauthorized privilege | Server-side authorization checks | Negative authorization tests |

## Assumptions

- Application is intentionally vulnerable for training.
- Environment is isolated.
- Testing is limited to the inventory.
- No production data is present.
- Availability testing is prohibited.
