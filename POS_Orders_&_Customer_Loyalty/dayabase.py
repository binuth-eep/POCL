from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
DATABASE_URL = (
 "postgres+psycopg://POCL:admin123@localhost:5432/"
)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(
 bind=engine,
 autoflush=False,
 autocommit=False
)
class Base(DeclarativeBase):
 pass
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
