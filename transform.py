import pandas as pd
from logs import log


def map_rockets(rockets_data):
    log("Mapping rocket IDs to rocket names")
    rocket_map = {}
    for rocket in rockets_data:
        rocket_map[rocket["id"]] = rocket["name"]
    return rocket_map


def clean_data(data):
    log(f"Cleaning {len(data)} launches")
    data_cleaned = []
    for launch in data:
        launch_info = {
            "name": launch.get("name"),
            "date_utc": launch.get("date_utc"),
            "success": launch.get("success"),
            "rocket": launch.get("rocket"),
            "details": launch.get("details"),
        }
        data_cleaned.append(launch_info)
    return data_cleaned


def make_df(data_cleaned, rocket_map):
    log("Building DataFrame from cleaned data")
    df_spacex = pd.DataFrame(data_cleaned)
    df_spacex["date_utc"] = pd.to_datetime(df_spacex["date_utc"])
    df_spacex["year"] = df_spacex["date_utc"].dt.year
    df_spacex["rocket"] = df_spacex["rocket"].apply(lambda x: rocket_map.get(x, "Unknown"))
    return df_spacex
