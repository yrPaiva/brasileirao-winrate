import matplotlib.pyplot as plt

def plot_static_winrate(df):
    plt.figure(figsize=(10,6))
    plt.bar(df['team'], df['win_rate'])
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Taxa de Vitória')
    plt.title('Win Rate dos Times (2020-2024)')
    plt.tight_layout()
    plt.show()