from app.models import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    parent_id = Column(Integer, ForeignKey(id))
    item = relationship("Item", back_populates="category")
