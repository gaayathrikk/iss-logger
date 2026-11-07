import csv, json, os, urllib.request
from datetime import datetime, timezone

URL = os.environ.get("ISS_URL", "http://api.open-notify.org/iss-now.json")
FILE = "iss_positions.csv"

data = json.load(urllib.request.urlopen(URL, timeout=15))
when = datetime.fromtimestamp(data["timestamp"], timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
row = [when, data["iss_position"]["latitude"], data["iss_position"]["longitude"], "LIVE"]

new = not os.path.exists(FILE)
with open(FILE, "a", newline="") as f:
    w = csv.writer(f)
    if new:
        w.writerow(["observed_at_utc", "latitude", "longitude", "freshness"])
    w.writerow(row)
print("saved", row)
