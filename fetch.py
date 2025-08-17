import pandas as pd
from soccerdata import FBref
import gspread
import google.auth

TEAMS = [
    "Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton",
    "Chelsea", "Crystal Palace", "Everton", "Fulham", "Ipswich Town",
    "Leicester City", "Liverpool", "Manchester City", "Manchester Utd",
    "Newcastle Utd", "Nott'ham Forest", "Southampton", "Tottenham",
    "West Ham", "Wolves"
]


def update_sheet(spreadsheet_id: str, worksheet_name: str, season: str = "2425"):
    # 1) Build dataframe from FBref (same idea as your script)   
    fbref = FBref(leagues=['ENG-Premier League'], seasons=[season])
    df = pd.concat([
        fbref.read_team_match_stats(stat_type="shooting", opponent_stats=True, team=team).assign(team=team)
        for team in TEAMS
    ], ignore_index=True)

    # 2) Get credentials from the Cloud Run service account via ADC
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    creds, _ = google.auth.default(scopes=SCOPES)
    gc = gspread.authorize(creds)

    # 3) Open target sheet + tab and write all at once (fastest)
    sh = gc.open_by_key(spreadsheet_id)
    try:
        ws = sh.worksheet(worksheet_name)
        ws.clear()
    except gspread.exceptions.WorksheetNotFound:
        ws = sh.add_worksheet(title=worksheet_name, rows="100", cols="26")

    values = [df.columns.tolist()] + df.astype(str).values.tolist()
    ws.update(values)
    return f"Rows written: {len(values)-1}"
