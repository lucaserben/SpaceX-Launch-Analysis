import os
from sqlalchemy import create_engine
from logs import log

def save_to_csv(df, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)

def create_connection():
    db_user = os.getenv("DB_USER", "postgres")
    db_pass = os.getenv("DB_PASSWORD", "postgres")
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "5432")
    db_name = os.getenv("DB_NAME", "spacex")
    engine = create_engine(
        f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    )
    print("Database connection established successfully")
    log("Database connection established successfully")
    return engine

def save_launches_to_db(df):
    engine = create_connection()
    df.to_sql("launches", con=engine, if_exists="replace", index=False)
    print("Data saved to PostgreSQL database successfully")
    log("Data saved to PostgreSQL database successfully")

