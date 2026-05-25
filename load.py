import os
from sqlalchemy import create_engine
from logs import log

def save_to_csv(df, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)

def create_connection():
    engine = create_engine(
        "postgresql+psycopg2://postgres:postgres@localhost:5432/spacex"
    )
    print("Database connection established successfully")
    log("Database connection established successfully")
    return engine

def save_launches_to_db(df):
    engine = create_connection()
    df.to_sql("launches", con=engine, if_exists="replace", index=False)
    print("Data saved to PostgreSQL database successfully")
    log("Data saved to PostgreSQL database successfully")

