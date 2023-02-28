from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
# from app.dotenv import db_host,db_port,db_name,db_user,db_password

# from .main import app
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:1234@localhost/fastapi'

# SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)


Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# @app.on_event('startup')
# def startup():
#     engine.connect()

# @app.on_event('shutdown')
# def shutdown():
#     SessionLocal.close_all()
#     engine.dispose()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# try:
#  conn = psycopg2.connect(database=db_name,user=db_user,host=db_host,password=db_password,cursor_factory=RealDictCursor)
#  cursor = conn.cursor()
#  print("'connection established successfuly'")
# except Exception as error :
#     print("fai in connecting to database")
#     print("the error was ",error)
