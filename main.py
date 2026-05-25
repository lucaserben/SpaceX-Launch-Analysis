import os

from extract import fetch
from logs import log
from transform import map_rockets, clean_data, make_df
from load import save_to_csv, save_launches_to_db
from analyst import (
    calculate_success_rate,
    success_rate_by_year,
    launches_per_year,
    success_rate_by_rocket,
    plot_success_rate_by_year,
    plot_launches_per_year,
    plot_success_rate_by_rocket,
)

# ============================================================================
# EXTRACT STAGE
# ============================================================================

log("Starting extract process")

os.makedirs("data", exist_ok=True)

launches_url = "https://api.spacexdata.com/v5/launches"
rockets_url = "https://api.spacexdata.com/v4/rockets"

response = fetch(launches_url)
if response.status_code == 200:
    data = response.json()
else:
    print("Failed to retrieve data from the API.")
    data = []

response_two = fetch(rockets_url)
if response_two.status_code == 200:
    rockets_data = response_two.json()
else:
    print("Failed to retrieve rocket data from the API.")
    rockets_data = []

# Tracking the rocket names with their IDs for later use in transformation
rocket_map = map_rockets(rockets_data)

log("Extract process finished")

# ============================================================================
# TRANSFORM STAGE
# ============================================================================

log("Starting transform process")

data_cleaned = clean_data(data)

# Transform data is stored in a DataFrame for further analysis
df_spacex = make_df(data_cleaned, rocket_map)

log("Transform process finished")

# ============================================================================
# LOAD STAGE
# ============================================================================

log("Starting load process")
save_to_csv(df_spacex, "data/spacex_launches.csv")
log("Starting database save process")
try:
    save_launches_to_db(df_spacex)
    log("Database save process finished")
except Exception as e:
    log(f"Error saving launches to database: {e}")

log("Load process finished")

# ============================================================================
# ANALYSIS STAGE
# ============================================================================

log("Starting analyst process")

# Calculate and print success rate
success_rate = calculate_success_rate(df_spacex)
print(f"SpaceX Success Rate: {success_rate}%",
      f"Total Launches: {len(df_spacex)}",
      f"None Success Entries: {df_spacex['success'].isna().sum()}")

# Calculate and plot success rate by year
success_rate_yearly = success_rate_by_year(df_spacex)
plot_success_rate_by_year(success_rate_yearly)

# Calculate and plot launches per year
launches_yearly = launches_per_year(df_spacex)
plot_launches_per_year(launches_yearly)

# Calculate and plot success rate by rocket
success_rate_rocket = success_rate_by_rocket(df_spacex)
plot_success_rate_by_rocket(success_rate_rocket)

log("Analyst process finished")


