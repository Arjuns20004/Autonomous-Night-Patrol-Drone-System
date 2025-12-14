
# map_server.py
# Live drone tracking dashboard using Flask + Leaflet

from flask import Flask, jsonify, render_template_string
from shared_state import get_state

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head>
<title>Drone Live Map</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
</head>
<body>
<h2>Night Patrol Drone - Live Tracking</h2>
<p id="battery"></p>
<div id="map" style="height:500px;"></div>

<script>
var map = L.map('map').setView([12.9716,77.5946],18);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
var marker = L.marker([12.9716,77.5946]).addTo(map);

setInterval(()=>{
fetch('/status').then(r=>r.json()).then(data=>{
marker.setLatLng([data.lat,data.lon]);
document.getElementById("battery").innerHTML =
"Battery: " + data.battery + "%";
});
},2000);
</script>
</body>
</html>
'''

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/status")
def status():
    return jsonify(get_state())

def start_map_server():
    app.run(debug=False)
