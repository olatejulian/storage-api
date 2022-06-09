import os
import dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

env_loaded = dotenv.load_dotenv()

if env_loaded is True:
    database_uri = os.getenv('DATABASE_URI')

    engine = create_engine(database_uri)

    Session = sessionmaker(engine)
