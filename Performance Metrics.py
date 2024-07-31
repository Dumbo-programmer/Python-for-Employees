import pandas as pd
import matplotlib.pyplot as plt

def performance_metrics():
    print("Welcome to the Performance Metrics Script!")
    data_file = input("Enter the path to the performance data file (CSV format): ")
    df = pd.read_csv(data_file)

    # Example: Generate performance metrics
    summary = df.describe()
    summary.to_csv("performance_summary.csv")
    print("Performance summary saved to performance_summary.csv")

    if input("Would you like to generate a performance plot? (y/n) ").lower() == "y":
        df.plot()
        plt.savefig("performance_plot.png")
        print("Performance plot saved.")

if __name__ == "__main__":
    performance_metrics()
