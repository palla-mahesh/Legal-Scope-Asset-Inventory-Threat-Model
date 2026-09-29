# Data Flow Diagram

```text
+------------------+       HTTP       +-------------------------+
| Kali Test Client | ----------------> | LAB-01 Flask Training   |
| Nmap / Browser   |                  | 127.0.0.1:8080         |
+------------------+                  +-----------+-------------+
                                                |
                                                | Application data
                                                v
                                      +-------------------------+
                                      | Local SQLite training   |
                                      | database                |
                                      +-------------------------+

Kali assessor -> evidence directory -> finding/report -> final submission

LAB-02:
Kali assessor -> 192.168.56.20
```

Graphviz source is provided in data_flow.dot.
