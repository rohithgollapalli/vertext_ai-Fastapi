from sqlalchemy import create_engine, Column, Integer, Text, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

# Masked database URL for security. Store credentials in environment variables or a config file in production.
DATABASE_URL = "mysql+pymysql://<username>:<password>@<host>:<port>/<database_name>"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative class definitions
Base = declarative_base()