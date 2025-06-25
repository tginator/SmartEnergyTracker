import pandas as pd
import matplotlib.pyplot as plt

def plot_usage():

    df = pd.read_csv('data/energy_usage.csv')

    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['usage_kWh'], marker='o', linestyle='-')
    plt.title('Daily Energy Usage Over Time')
    plt.xlabel('Date')
    plt.ylabel('Energy Usage (kWh)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_usage()