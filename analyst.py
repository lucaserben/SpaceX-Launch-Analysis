import matplotlib.pyplot as plt
from logs import log

def calculate_success_rate(df):
    log("Calculating overall success rate")
    df_valid=df[df["success"].notna()]
    success_rate = df_valid["success"].mean() * 100
    return round(success_rate, 2)


def success_rate_by_year(df):
    log("Calculating success rate by year")
    df_valid = df[df["success"].notna()]
    success_rate_yearly = df_valid.groupby("year")["success"].mean() * 100
    return success_rate_yearly.round(2)

def launches_per_year(df):
    log("Calculating launches per year")
    launches_yearly = df.groupby("year").size()
    return launches_yearly

def success_rate_by_rocket(df):
    log("Calculating success rate by rocket")
    df_valid = df[df["success"].notna()]
    success_rate_rocket = df_valid.groupby("rocket")["success"].mean() * 100
    return success_rate_rocket.round(2)


def plot_success_rate_by_year(data):
    log("Plotting success rate by year")
    plt.figure(figsize=(10, 5))
    plt.plot(
        data.index,
        data.values,
        marker="o"
    )
    plt.title("SpaceX Success Rate by Year")
    plt.xlabel("Year")
    plt.ylabel("Success Rate (%)")
    plt.grid(True)
    plt.show()


def plot_launches_per_year(data):
    log("Plotting launches per year")
    plt.figure(figsize=(12, 6))
    plt.bar(
        data.index,
        data.values
    )
    plt.title("SpaceX Launches per Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Launches")
    plt.grid(axis="y")
    plt.show()


def plot_success_rate_by_rocket(data):
    log("Plotting success rate by rocket")
    plt.figure(figsize=(10, 6))
    plt.bar(
        data.index,
        data.values
    )
    plt.title("SpaceX Success Rate by Rocket")
    plt.xlabel("Rocket")
    plt.ylabel("Success Rate (%)")
    plt.ylim(0, 100)
    plt.grid(axis="y")
    plt.show()