#!/usr/bin/env python3
"""Simple Flask dashboard for the Raspberry Pi Wi-Fi extender."""

import platform
from flask import Flask, jsonify, render_template_string

from monitor import get_connected_clients, get_signal_strength

app = Flask(__name__)

PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="refresh" content="10">
  <title>RPi Wi-Fi Extender Dashboard</title>
  <style>
    body { font-family: Arial, sans-serif; background: #101827; color: #f4f7fb;
           margin: 0; padding: 28px; }
    h1 { color: #5eead4; }
    .card { background: #1e293b; border-radius: 10px; padding: 20px;
            margin: 14px 0; max-width: 720px; }
    .value { font-size: 1.35rem; color: #7dd3fc; overflow-wrap: anywhere; }
    li { margin: 8px 0; }
    .muted { color: #aab7c8; }
  </style>
</head>
<body>
  <h1>Wi-Fi Range Extender</h1>
  <p class="muted">Raspberry Pi network status · refreshes every 10 seconds</p>
  <section class="card">
    <h2>Upstream Wi-Fi signal</h2>
    <p class="value">{{ signal }}</p>
  </section>
  <section class="card">
    <h2>Connected clients ({{ clients|length }})</h2>
    {% if clients %}
      <ul>{% for client in clients %}<li>{{ client }}</li>{% endfor %}</ul>
    {% else %}
      <p class="muted">No connected clients reported by hostapd.</p>
    {% endif %}
  </section>
  <p class="muted">Device: {{ hostname }}</p>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(
        PAGE,
        clients=get_connected_clients(),
        signal=get_signal_strength(),
        hostname=platform.node(),
    )


@app.route("/api/status")
def api_status():
    return jsonify({
        "clients": get_connected_clients(),
        "client_count": len(get_connected_clients()),
        "signal": get_signal_strength(),
        "hostname": platform.node(),
    })


if __name__ == "__main__":
    # Bind to the AP network so connected clients can reach the dashboard.
    app.run(host="0.0.0.0", port=5000, debug=False)
