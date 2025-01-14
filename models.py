import sqlalchemy as sq
from sqlalchemy import CheckConstraint
from sqlalchemy.orm import declarative_base, relationship
from datetime import date


Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publishers'

    id = sq.Column(sq.Integer, primary_key = True)
    name = sq.Column(sq.String(length = 255), unique = True, nullable = False)
    books = relationship('Book', backref = 'publisher')

class Book(Base):
    __tablename__ = 'books'

    id = sq.Column(sq.Integer, primary_key = True)
    title = sq.Column(sq.String(length = 255), unique = True, nullable = False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publishers.id'),
                             nullable = False)
    stocks = relationship('Stock', backref = 'book')


class Stock(Base):
    __tablename__ ='stocks'

    id = sq.Column(sq.Integer, primary_key = True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('books.id'))
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shops.id'))
    count = sq.Column(sq.Integer)
    __table_args__ = (CheckConstraint('count >= 0',
                                       name='check_count_non_negative'),)
    shop = relationship('Shop', backref = 'stocks')
    sales = relationship('Sale', backref = 'stock')


class Shop(Base):
    __tablename__ ='shops'

    id = sq.Column(sq.Integer, primary_key = True)
    name = sq.Column(sq.String(length = 255), nullable = False)


class Sale(Base):
    __tablename__ ='sales'

    id = sq.Column(sq.Integer, primary_key = True)
    price = sq.Column(sq.Float)
    date_sale = sq.Column(sq.Date)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stocks.id'))
    count = sq.Column(sq.Integer)
    __table_args__ = (
                      CheckConstraint('count >= 0',
                                      name='check_count_non_negative'),
                      CheckConstraint('price >= 0',
                                      name='check_price_non_negative')
    )

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


