from rich.console import Console
from rich.table import Table

class PlayerStats:
    def __init__(self, player_reader):
        self.player_reader = player_reader 

    def top_scorers_by_nationality(self, nationality, season):
        players = self.player_reader.get_players(season)
        filtered_players = [player for player in players if player.nationality == nationality]
        return sorted(filtered_players, key=lambda p: p.points, reverse=True)
        
    def display_players(self, players):
        console = Console()
        table = Table(title="Top Scorers")

        
        table.add_column("Player", style="dodger_blue3")
        table.add_column("Team", style="purple4")
        table.add_column("Goals", style="red3")
        table.add_column("Assists", style="bright_blue")
        table.add_column("Points", style="bold green")

        for player in players:
            table.add_row(str(player.name), player.team, f"{player.goals}", f"{player.assists}", f"{player.points}")

        
        console.print(table)