import pandas as pd

def load_matches(path: str = 'data/campeonato-brasileiro-full.csv',
                 years: list[int] = [2020, 2021, 2022, 2023, 2024]) -> pd.DataFrame:
    """
    Carrega CSV, converte data, filtra Série A e anos desejados.
    Retorna DataFrame com colunas: year, team, gf, ga.
    """
    df = pd.read_csv(path, dtype={'data': str})
    df['date'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
    df['year'] = df['date'].dt.year
    df = df[df['year'].isin(years)]
    # monta jogos para mandante
    home = df[['year','mandante','mandante_Placar','visitante_Placar']].rename(
        columns={'mandante':'team','mandante_Placar':'gf','visitante_Placar':'ga'}
    )
    # e visitante
    away = df[['year','visitante','visitante_Placar','mandante_Placar']].rename(
        columns={'visitante':'team','visitante_Placar':'gf','mandante_Placar':'ga'}
    )
    return pd.concat([home, away], ignore_index=True)
