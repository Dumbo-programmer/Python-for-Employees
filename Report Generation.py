import pandas as pd
import matplotlib.pyplot as plt

def generate_report():
    print("Welcome to the Report Generation Script!")
    data_file = input("Enter the path to the data file (CSV format): ")
    df = pd.read_csv(data_file)
    
    report_file = input("Enter the path to save the report: ")
    
    # Generate a simple report
    df.describe().to_csv(report_file)
    print(f"Report generated and saved to {report_file}")

    # Optional: Generate a plot
    if input("Would you like to generate a plot? (y/n) ").lower() == "y":
        df.plot()
        plt.savefig(report_file.replace(".csv", ".png"))
        print("Plot saved.")

if __name__ == "__main__":
    generate_report()
