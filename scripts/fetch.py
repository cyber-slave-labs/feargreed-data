"""CNN Fear & Greed 지수를 수집해서 data.json으로 저장한다."""
import json
import sys
import urllib.request
from datetime import datetime, timezone

URL = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata/2021-01-01"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

req = urllib.request.Request(URL, headers={
    "User-Agent": UA,
    "Accept": "application/json",
    "Referer": "https://edition.cnn.com/markets/fear-and-greed",
})
with urllib.request.urlopen(req, timeout=30) as res:
    raw = json.load(res)

points = raw["fear_and_greed_historical"]["data"]
series = {}
for p in points:  # 같은 날짜 중복 시 마지막 값 사용
    date = datetime.fromtimestamp(p["x"] / 1000, tz=timezone.utc).strftime("%Y-%m-%d")
    series[date] = round(float(p["y"]), 2)

rows = sorted(series.items())
if len(rows) < 100:
    sys.exit(f"too few points: {len(rows)}")

out = {
    "source": "cnn-fear-greed",
    "updatedAt": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "latest": {"date": rows[-1][0], "value": rows[-1][1]},
    "series": rows,
}
with open("data.json", "w") as f:
    json.dump(out, f, separators=(",", ":"))

print(f"OK {len(rows)} points, latest {rows[-1][0]} = {rows[-1][1]}")
