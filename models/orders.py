from sqlalchemy import Integer, DateTime, ForeignKey, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

from models.product import Product

Base = declarative_base()


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    data = Column(DateTime)
    product_id = Column(Integer, ForeignKey('product_id'))
    user_id = Column(Integer)

    products = relationship(
        Product,
        backref=backref('orders',
                        uselist=True,
                        cascade='delete, all'))

    def __str__(self):
        return f"{self.quantity} {self.data}"
