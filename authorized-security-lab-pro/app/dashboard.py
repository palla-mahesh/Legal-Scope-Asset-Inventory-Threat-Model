from flask import Flask, render_template_string
from pathlib import Path
import csv, json

app = Flask(__name__)
ROOT = Path(__file__).resolve().parents[1]

HTML = '''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Authorized Security Lab — Pro Dashboard</title>
<style>
body{font-family:Arial,sans-serif;background:#111827;color:#e5e7eb;margin:0}
main{max-width:1100px;margin:40px auto;padding:0 20px}
.card{background:#1f2937;border:1px solid #374151;border-radius:12px;padding:20px;margin:16px 0}
.muted{color:#9ca3af}
table{width:100%;border-collapse:collapse}
td,th{padding:10px;border-bottom:1px solid #374151;text-align:left}
.badge{padding:4px 8px;border-radius:999px;background:#064e3b;color:#a7f3d0}
code{color:#f9a8d4}
</style>
</head>
<body><main>
<h1>Authorized Security Lab — Pro Dashboard</h1>
<p class="muted">Documentation and scope visibility only.</p>
<div class="card"><h2>Approved Assets</h2>
<table><tr><th>ID</th><th>Name</th><th>Target</th><th>Status</th></tr>
{% for r in rows %}
<tr><td>{{r.asset_id}}</td><td>{{r.asset_name}}</td>
<td><code>{{r.ip_or_url}}</code></td>
<td><span class="badge">{{r.testing_allowed}}</span></td></tr>
{% endfor %}
</table></div>
<div class="card"><h2>Stop Conditions</h2><ul>
{% for s in engagement.stop_conditions %}<li>{{s}}</li>{% endfor %}
</ul></div>
<div class="card"><h2>Deliverables</h2>
<ul>
<li>Authorized lab dossier</li>
<li>Asset inventory</li>
<li>Data-flow diagram</li>
<li>STRIDE register</li>
<li>Rules of engagement</li>
<li>Evidence/report templates</li>
</ul></div>
</main></body></html>
'''

@app.route("/")
def dashboard():
    with open(ROOT / "config/asset_inventory.csv", newline="") as f:
        rows = list(csv.DictReader(f))
    with open(ROOT / "config/engagement.json") as f:
        engagement = json.load(f)
    return render_template_string(HTML, rows=rows, engagement=engagement)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9090, debug=False)
