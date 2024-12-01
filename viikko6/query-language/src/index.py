from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or, Pinorakentaja

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )

    matcher = And(
    Not(HasAtLeast(2, "goals")),
    PlaysIn("NYR")
    )

    matcher = Or(
    HasAtLeast(45, "goals"),
    HasAtLeast(70, "assists")
    )

    matcher = And(
    HasAtLeast(70, "points"),
    Or(
        PlaysIn("NYR"),
        PlaysIn("FLA"),
        PlaysIn("BOS")
    )
)

    rakenna = Pinorakentaja()

    matcher = rakenna.plays_in("NYR").pino()



    matcher = (
      rakenna
      .plays_in("NYR")
      .has_at_least(10, "goals")
      .has_fewer_than(20, "goals")
      .pino()
    )

    for player in stats.matches(matcher):
        print(player)

    rakenna = Pinorakentaja()
    m1 = (
        rakenna
        .plays_in("PHI")
        .has_at_least(10, "assists")
        .has_fewer_than(10, "goals")
        .pino()
)

    m2 = (
        rakenna
        .plays_in("EDM")
        .has_at_least(50, "points")
        .pino()
)
    matcher = (
        rakenna
            .one_of(
                rakenna.plays_in("PHI")
                    .has_at_least(10, "assists")
                    .has_fewer_than(10, "goals")
                    .pino(),
                rakenna.plays_in("EDM")
                    .has_at_least(50, "points")
                    .pino()
        )
        .pino()
)

    matcher = rakenna.one_of(m1, m2).pino()

    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
