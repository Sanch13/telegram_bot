from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

from models.category import Category

Base = declarative_base


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    title = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    is_active = Column(Boolean)
    category_id = Column(Integer, ForeignKey('category.id'))

    category = relationship(
        Category,
        backref=backref('product',
                        uselist=True,
                        cascade='delete, all'))

    def __str__(self):
        return f"{self.name} {self.title} {self.price}"
