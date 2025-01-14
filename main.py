import configparser
import psycopg2
from psycopg2 import Error
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Stock, Sale, Shop

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('settings.ini')
    db_name = config['Tokens']['db_name']
    user = config['Tokens']['user']
    password = config['Tokens']['password']
    host = config['Tokens']['host']
    port = config['Tokens']['port']

    DSN = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'
    engine = sqlalchemy.create_engine(DSN)

    create_tables(engine)

    Session = sessionmaker(bind = engine)
    session = Session()














    session.close()