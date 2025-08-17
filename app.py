import os
from flask import Flask, jsonify, request
from fetch import update_sheet

app = Flask(__name__)

SPREADSHEET_ID = os.environ["1L1z3hH4jis3Y9Lyoaeu7-tQzLX2cBYesp_Hzy51iUBo"]
WORKSHEET_NAME = os.environ.get("WORKSHEET_NAME", "PL2425 Shooting")
DEFAULT_SEASON = os.environ.get("SEASON", "2425")


@app.get("/healthz")
def healthz():
    return "ok", 200


@app.post("/run")
@app.get("/run")
def run():
    season = request.args.get("season", DEFAULT_SEASON)
    result = update_sheet(SPREADSHEET_ID, WORKSHEET_NAME, season)
    return jsonify({"status": "ok", "season": season, "result": result}), 200
