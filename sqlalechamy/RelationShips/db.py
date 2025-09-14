from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

DATABASE_URL = "sqlite:///mydb.db"
engine=create_engine(DATABASE_URL,echo=True)
SessionLocal=sessionmaker(bind=engine,autoflush=False)

Base=declarative_base()