from app.models import Base, Category
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    price = Column(Float)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    category = relationship("Category", back_populates="item")
