import pandas as pd
from data_loader import load_matches

def compute_winrates(years: list[int]) -> pd.DataFrame:
    """
    Para cada time:
      - games = total de partidas
      - wins  = partidas em que gf > ga
      - win_rate = wins / games
    Retorna DataFrame ordenado por win_rate desc.
    """
    all_games = load_matches(years=years)
    all_games['win'] = all_games['gf'] > all_games['ga']
    summary = all_games.groupby('team').agg(
        games=('win','size'),
        wins =('win','sum')
    ).reset_index()
    summary['win_rate'] = summary['wins'] / summary['games']
    return summary.sort_values('win_rate', ascending=False)
