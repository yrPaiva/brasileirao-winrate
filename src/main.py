from analysis import compute_winrates
from viz import plot_static_winrate

def main():
    years = [2020, 2021, 2022, 2023, 2024]
    df = compute_winrates(years)
    print(df.to_string(index=False, float_format='%.3f'))
    plot_static_winrate(df)

if __name__ == '__main__':
    main()
