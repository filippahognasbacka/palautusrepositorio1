from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/"
    season = input("Select season ")
    nationality = input("Select nationality ")
    
    
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality, season)

    print(f"Top scorers from {nationality} in {season}: ")
    stats.display_players(players)

if __name__ == "__main__":
    main()
