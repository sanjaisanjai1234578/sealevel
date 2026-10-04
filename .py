import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color="blue", label="Original Data")

    # Create first line of best fit (all available data extending to 2050)
    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred1 = pd.Series([i for i in range(1880, 2051)])
    y_pred1 = res_all.slope * x_pred1 + res_all.intercept
    ax.plot(x_pred1, y_pred1, "r", label="Fit: 1880-2050")

    # Create second line of best fit (data from year 2000 onwards extending to 2050)
    df_recent = df[df["Year"] >= 2000]
    res_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x_pred2 = pd.Series([i for i in range(2000, 2051)])
    y_pred2 = res_recent.slope * x_pred2 + res_recent.intercept
    ax.plot(x_pred2, y_pred2, "green", label="Fit: 2000-2050")

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save plot and return data for testing
    plt.savefig("sea_level_plot.png")
    return ax
