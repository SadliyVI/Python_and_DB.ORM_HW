import json
from datetime import datetime
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

    with open('fixtures/test_data.json') as f:
        data = json.load(f)

    for item in data:
        model = item['model']
        pk = item['pk']
        fields = item['fields']

        if model == 'publisher':
            publisher = Publisher(id = pk, name = fields['name'])
            session.add(publisher)
        elif model == 'book':
            book = Book(id = pk, title = fields['title'],
                        id_publisher = fields['id_publisher'])
            session.add(book)
        elif model == 'shop':
            shop = Shop(id = pk, name = fields['name'])
            session.add(shop)
        elif model == 'stock':
            stock = Stock(id = pk, id_book = fields['id_book'],
                          id_shop = fields['id_shop'], count = fields['count'])
            session.add(stock)
        elif model == 'sale':
            date_sale = datetime.strptime(fields['date_sale'],
                                          '%Y-%m-%dT%H:%M:%S.%fZ').date()
            sale = Sale(id = pk, price = fields['price'], date_sale =
            date_sale, id_stock = fields['id_stock'], count = fields['count'])
            session.add(sale)
    session.commit()








    session.close()