from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime

Base = declarative_base()

class DiscountModel(Base):
    __tablename__ = "discounts"
    id = Column(Integer, autoincrement=True, primary_key=True)
    code = Column(String(50), nullable=False, unique=True)
    description = Column(String(255), nullable=True)

    is_active = Column(Boolean, default=True) 

    is_deleted = Column(Boolean, default=False) 

    deleted_at = Column(DateTime, nullable=True)
