"""
English Premier League simulation game by Miroslava Ezel N1161732
"""

while True:
    epl_game = input("\tDo you want The English Premier League game? (y/n): ")
    if epl_game == "y":
        # Print heading and start the game for epl.
        print("\n WELCOME TO THE ENGLISH PREMIER LEAGUE 2022/23 SEASON")
        print("=" * 55)
        print("\n\t\t" + "\t" + "The EPL teams:")
        print("\t\t" + "=" * 10 + "=" * 8)
        break

    elif epl_game == "n":
        print("\tI thought you wanted to see the EPL! You can try again.")
        continue

    else:
        print("\tSorry. You have entered an incorrect response. Please enter 'y' or 'n' to continue. ")

# Import all the classes and functions from Teams module.

from Team import *

# Load teams from file
epl = load_teams_fr_file()

print("")
print(epl)
print("")
print("=" * 55)

# Print club and their managers.

managers = input("\nDo you want to see the teams managers? (y/n):")
if managers == "y":
    print("\n\tPremier League Clubs and their manager:")
    print("=" * 45)
    print("  CLUB\t\t\t\t\t\t MANAGER")
    print("")
elif managers == "n":
    print("\tThat is too bad. Maybe next time!")
else:
    print("\tSorry. You have entered an incorrect response. Please enter 'y' or 'n' to continue. ")
if managers == "y":
    # Import all the classes and functions from Managers module.

    from Managers import *

    # Load managers from a file and print their club and name.

    mg = load_managers_fr_file()
    # I have used the end= as this was printing empty line between rows.
    # Print each manager's club and name, with the club name taking up 25 spaces.
    if mg:
        for m in mg:
            print(f"{m.club.ljust(25)}\t{m.manager}", end='')

# Open the text file of top three players and then close it.

try:
    with open("top_players.txt", "r") as f:
        top_three_data = f.readlines()
except FileNotFoundError:
    print("File not found!")
finally:
    f.close()

# Parse the top three player data and create a list.

top_players = [player.strip() for player in top_three_data]

# Import the random module, which provides functions for generating random numbers.

import random

# Read team names from file and close the file

try:
    with open('epl.txt') as f:
        teams = [line.strip() for line in f]
except FileNotFoundError:
    print("File not found!")
finally:
    f.close()

# Define constants for number of matches, points for a win or draw.

NUM_MATCHES = 38
WIN_POINTS = 3
DRAW_POINTS = 1

# Initialize dictionaries to keep track of points, wins, draws, and losses.

points = {team: 0 for team in teams}
wins = {team: 0 for team in teams}
draws = {team: 0 for team in teams}
losses = {team: 0 for team in teams}

# Simulate matches

for i in range(NUM_MATCHES):
    for home_team in teams:
        away_team = random.choice(teams)
        while away_team == home_team:
            away_team = random.choice(teams)
        home_score = random.randint(0, 4)
        away_score = random.randint(0, 4)
        if home_score > away_score:
            points[home_team] += WIN_POINTS
            wins[home_team] += 1
            losses[away_team] += 1
        elif home_score < away_score:
            points[away_team] += WIN_POINTS
            wins[away_team] += 1
            losses[home_team] += 1
        else:
            points[home_team] += DRAW_POINTS
            points[away_team] += DRAW_POINTS
            draws[home_team] += 1
            draws[away_team] += 1

# Sort teams based on points
sorted_teams = sorted(teams, key=lambda x: (-points[x], -wins[x], -draws[x], x))

# Ask if I want to see the EPL table.

epl_table = input("\nWould you like to see the EPL table? (y/n):")
if epl_table == "y":
    # Print the final league table
    print(f"\n{'=' * 55}\n\t\t{'Premier League Table 2022/23':^43}\n{'=' * 55}\n")

    print("Pos\t Team\t\t             Pt\t\tW\t\tD\t\tL")
    for i, team in enumerate(sorted_teams):
        team_name = team.split(":")[0].split("-")[0].strip()  # split by ":" or "-" and select first element
        print(f"{i + 1}\t{team_name.ljust(20)}\t{points[team]}\t\t{wins[team]}\t\t{draws[team]}\t\t{losses[team]}")

else:
    print("\tYou have missed out on the results!")

players = input("\nDo you want to see the top three players in the 2022/23 season? (y/n):")
if players == "y":

    # Print top three players form a list.

    print("\nThe top three Premier League players this season are:")
    print("=" * 55)
    # Enumerate is a function that keeps track of a position.
    for i, player in enumerate(top_players):
        print(f"{i + 1}. {player}")
else:
    print("\tYou have missed your chance!")

# Ask if the user wants to relegate the bottom team

relegate = input("\nWould you like to relegate the bottom team? (y/n): ")
if relegate.lower() == "y":
    relegate_team_name = sorted_teams[-1].split(":")[0].split("-")[0].strip()
    print(f"\n{relegate_team_name} has been relegated.")
    sorted_teams = sorted_teams[:-1]

# Print the winner of the season.

winner_name = sorted_teams[0].split(":")[0].split("-")[0].strip()
print(f"\nThe winner of the 2022/23 season is {winner_name}!")

