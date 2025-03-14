import pandas as pd
from soccerdata import FBref


# Initialize the FBref API
fbref = FBref(leagues=['ENG-Premier League'], seasons=['2425'])

# List of teams
teams = [
    "Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton", 
    "Chelsea", "Crystal Palace", "Everton", "Fulham", "Ipswich Town", 
    "Leicester City", "Liverpool", "Manchester City", "Manchester Utd", 
    "Newcastle Utd", "Nott'ham Forest", "Southampton", "Tottenham", 
    "West Ham", "Wolves"
]


# Retrieve and combine data, adding 'team' column
stats_shooting = pd.concat([
    fbref.read_team_match_stats(stat_type="shooting", opponent_stats=True, team=team).assign(team=team)
    for team in teams
], ignore_index=True)
stats_shooting.to_csv("Premier_League_Shooting.csv", index=False)
print("Shooting data saved to csv")

stats_passing = pd.concat([
    fbref.read_team_match_stats(stat_type="passing", opponent_stats=True, team=team).assign(team=team)
    for team in teams
], ignore_index=True)
stats_passing.to_csv("Premier_League_Passing.csv", index=False)
print("Passing data saved to csv")

stats_passing_types = pd.concat([
    fbref.read_team_match_stats(stat_type="passing_types", opponent_stats=True, team=team).assign(team=team)
    for team in teams
], ignore_index=True)
stats_passing_types.to_csv("Premier_League_Passing_Types.csv", index=False)
print("Passing Types data saved to csv")

stats_possession = pd.concat([
    fbref.read_team_match_stats(stat_type="possession", opponent_stats=True, team=team).assign(team=team)
    for team in teams
], ignore_index=True)
stats_possession.to_csv("Premier_League_Posession.csv", index=False)
print("Possession data saved to csv")

stats_misc = pd.concat([
    fbref.read_team_match_stats(stat_type="misc", opponent_stats=True, team=team).assign(team=team)
    for team in teams
], ignore_index=True)
stats_misc.to_csv("Premier_League_Misc.csv", index=False)
print("Misc data saved to csv")


stats_defense = pd.concat([
    fbref.read_team_match_stats(stat_type="defense", opponent_stats=True, team=team).assign(team=team)
    for team in teams
], ignore_index=True)
stats_defense.to_csv("Premier_League_Defense.csv", index=False)
print("Defense data saved to csv")

# stats_schedule = pd.concat([
#     fbref.read_team_match_stats(stat_type="schedule", opponent_stats=True, team=team).assign(team=team)
#     for team in teams
# ], ignore_index=True)
# stats_schedule.to_csv("Premier_League_Schedule.csv", index=False)
# print("Schedule data saved to csv")
